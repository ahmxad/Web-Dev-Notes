// EXPRESS
const express = require("express")
const app = express()
const path = require("path")
// EJS
app.set("view engine", "ejs")
app.set("views", path.join(__dirname, "/views"))
// PORT
let PORT = 3000;
app.listen(PORT, ()=>{
    console.log(`Running at ${PORT} 🐥`)
})
// HOME
app.get("/ig/:username", (req, res)=>{
    let {username} = req.params;
    let val = Math.floor(Math.random()*6)+1;
    res.render("home", {username, val})
})