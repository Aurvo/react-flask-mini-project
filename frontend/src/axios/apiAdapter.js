import axios from 'axios'

function getData(params, callback) {
    axios.get('http://localhost:8000/api', {
        params: params
    })
    .then(callback)
    .catch(function (error) {
        console.log(error);
    }); 
}

export default getData;