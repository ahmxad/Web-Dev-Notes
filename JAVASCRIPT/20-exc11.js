const fs = require("node:fs")
const process1 = process.argv;
if (process1[2] === "add"){
    fs.appendFileSync('file.txt', `${process1[3]}\n`, 'utf-8')
    console.log(`Note '${process1[3]}' has been added`)
}
if (process1[2]==="list"){
    const readF = fs.readFileSync('file.txt', "utf-8");
    console.log(readF)
}
if (process1[2] === "delete") {
    const readF = fs.readFileSync('file.txt', 'utf-8');
    const notes = readF.split('\n');
    const filtered = notes.filter(note => note !== process1[3]);
    fs.writeFileSync('file.txt', filtered.join('\n'), 'utf-8');
    console.log("Note deleted");
}