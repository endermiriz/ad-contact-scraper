const express = require('express');
const createError = require('http-errors');
const morgan = require('morgan');
// const fs = require('fs');
const { Client, LocalAuth } = require('whatsapp-web.js');
const qrcode = require('qrcode-terminal')
require('dotenv').config();
const cors = require('cors');


const client = new Client({
  authStrategy: new LocalAuth({
    clientId: "client-one"
  }),
  puppeteer: {
    headless: true,
  }
});

client.initialize();


const corsOptions ={
  origin:'http://localhost:3000', 
  credentials:true,            //access-control-allow-credentials:true
  optionSuccessStatus:200
}


const app = express();
app.use(express.json());
app.use(express.urlencoded({ extended: false }));
app.use(morgan('dev'));


app.use(cors(corsOptions));

let qrData = '';
client.on('qr', qr => {
  console.log('QR RECEIVED', qr);
  qrData = qr;
  qrcode.generate(qr, { small: true });
});
app.get('/getqr', async(req, res, next) => {
  try{
    res.header("Access-Control-Allow-Origin", "*")
    res.send({qrData});
  }
  catch(err){
    next(err)
  }
  });

client.on('authenticated', (session) => {
  console.log('WHATSAPP WEB => Authenticated');
});

client.on('auth_failure', msg => {
  console.error('AUTHENTICATION FAILURE', msg);
});

client.on('ready', () => {
  console.log('READY');
  qrData = "";
});


app.get('/', function(req, res){
  res.sendFile(__dirname + "/index.html");
});
app.post('/sendmessage', async (req, res, next) => {
  try {
    res.header('Access-Control-Allow-Origin', 'http://localhost:8000/');
    res.header('Access-Control-Allow-Credentials', true);
    res.header('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE');
    res.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept");
    res.header("Access-Control-Allow-Origin", "*")
    const { number, message } = req.body;
    const msg = await client.sendMessage(`${number}@c.us`, message); 
    res.send({ msg });
  } catch (error) {
    next(error);
  }
});

app.use((req, res, next) => {
  next(createError.NotFound());
});

app.use((err, req, res, next) => {
  res.status(err.status || 500);
  res.send({
    status: err.status || 500,
    message: err.message,
  });
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => console.log(`🚀 @ http://localhost:${PORT}`));
