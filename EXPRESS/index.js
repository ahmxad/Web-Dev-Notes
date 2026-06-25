// EXPRESS
const express = require("express")
const app = express()
const path = require("path")
let PORT = 3000;

app.use(express.static(path.join(__dirname, "public")))

app.listen(PORT, ()=>{
    console.log(`Running at ${PORT} 🐥`)
})