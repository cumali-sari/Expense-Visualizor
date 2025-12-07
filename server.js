const express = require('express');
const multer= require('multer');
const app = express();
const PORT = 3000;
const upload= multer({dest: "uploads/"});

app.use(express.static('public'));

app.post("/upload", upload.single("file"), (req, res) => {
    res.send("File received: " + req.file.originalname);
});

app.listen(PORT, ()=>{
    console.log('Server running');
});