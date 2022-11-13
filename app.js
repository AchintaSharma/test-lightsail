const express = require('express');
const app = express();

app.use(express.json());


app.get('/', (req, res) => {
    res.status(200).send('Success!')
});

app.post('/data', (req, res) => {
    console.log(data);
    res.status(201).send('ok');
})


app.listen(3000, () => {
    console.log('app running on port 3000');
})