const express = require('express')
const {createBot, createProvider, createFlow, addKeyword } = require('@bot-whatsapp/bot')
const BaileysProvider = require('@bot-whatsapp/provider/baileys')
const MockAdapter = require('@bot-whatsapp/database/mock')
const flowPrincipal = require('./chatbot/index')

const app = express()
const port = process.env.PORT || 3001

app.use(express.json)
flowPrincipal

app.listen(port, ()=>{
    console.log(`Server listening on http://localhost:${port}`)
})