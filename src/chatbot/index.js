const { createBot, createProvider, createFlow, addKeyword, addChild } = require('@bot-whatsapp/bot')
const QRPortalWeb = require('@bot-whatsapp/portal')
const BaileysProvider = require('@bot-whatsapp/provider/baileys')
const MockAdapter = require('@bot-whatsapp/database/mock')
const axios = require('axios')



const flowRegistro = addKeyword(['1', 'registro', 'registrar'])
    .addAnswer('Hola, este es tu chatbot para registrarte y votar en la asamblea, necesito algunos datos.')
    .addAnswer('¿Cuál es tu nombre completo?', { capture: true }, async (ctx, { flowDynamic, gotoFlow }) => {
        console.log(ctx.body)

        const nombre = ctx.body
        // const response = await axios.post('http://localhost:8000/users/register', { nombre })
        // if (response.data.success) {
        return flowDynamic(`Gracias ${nombre}, has sido registrado correctamente.`)
        // } else {
        //    return flowDynamic('Hubo un error en el registro. Por favor, intenta de nuevo.')
        // }
    }).addAnswer(`Continuaras con el proceso de votación!`)
    .addAnswer(
        [`Continuaras con el proceso de votación!`],
        { capture: false },
        async (ctx, { flowDynamic, gotoFlow }) => {
            return gotoFlow(flowRealizarVotacion)
        }
    )

const flowVotacion = addKeyword(['2', 'votar', 'votacion'])
    .addAnswer('Antes de votar, necesitamos verificar tu identidad y ubicación.')
    .addAnswer('Por favor, comparte tu ubicación actual.', { capture: true }, async (ctx, { flowDynamic, gotoFlow }) => {
        if (ctx.message.location) {
            const { latitude, longitude } = ctx.message.location
            const response = await axios.post('http://localhost:8000/votes/validate-location', { latitude, longitude })
            if (response.data.valid) {
                return gotoFlow(flowRealizarVotacion)
            } else {
                return flowDynamic('Lo siento, no estás en la ubicación permitida para votar.')
            }
        } else {
            return flowDynamic('No se recibió la ubicación. Por favor, intenta de nuevo.')
        }
    })

const flowRealizarVotacion = addKeyword(['realizar_votacion'])
    .addAnswer('¿Cuál es tu opción de voto? (A, B, C)', { capture: true }, async (ctx, { flowDynamic }) => {
        const voto = ctx.body
        const response = await axios.post('http://localhost:8000/votes/submit', { voto })
        if (response.data.success) {
            return flowDynamic('Tu voto ha sido registrado correctamente.')
        } else {
            return flowDynamic('Hubo un error al registrar tu voto. Por favor, intenta de nuevo.')
        }
    })

const flowResultados = addKeyword(['3', 'resultados', 'ver resultados'])
    .addAnswer('Consultando los resultados...', null, async (ctx, { flowDynamic }) => {
        const response = await axios.get('http://localhost:8000/reports/results')
        return flowDynamic(`Resultados actuales:\n${JSON.stringify(response.data, null, 2)}`)
    })

const flowPrincipal = addKeyword(['hola', 'ole', 'alo'])
    .addAnswer('🙌 Hola, bienvenido al sistema de votaciones')
    .addAnswer(
        [
            'Elige una opción:',
            '1️⃣ Registrarse',
            '2️⃣ Votar',
            '3️⃣ Ver resultados'
        ],
        null,
        null,
        [flowRegistro, flowVotacion, flowResultados]
    )

const main = async () => {
    const adapterDB = new MockAdapter()
    const adapterFlow = createFlow([flowRegistro, flowVotacion, flowResultados, flowPrincipal])
    const adapterProvider = createProvider(BaileysProvider)

    createBot({
        flow: adapterFlow,
        provider: adapterProvider,
        database: adapterDB,
    })

    QRPortalWeb()
}


main()