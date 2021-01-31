<template>
  <div id="app">
    <Header/>
    <Articles :articles="articles"/>
  </div>

  
</template>

<script>
import Header from './components/Header';
import Articles from './components/Articles';
const axios = require('axios');

axios.get('http://127.0.0.1:5000',{
  number: 12
}).then(resp => {

    console.log(resp.data);
    console.log(resp.id)
});




export default {
  name: 'App',
  components: {
    Header,
    Articles
   
  },
  data(){
    return {
      articles: [{
        id: 1,
        title: "cute kittens",
        link: "poop.com",
        content: "blahablhablhablabhlabhlahbhla"

      },{
        id: 2,
        title: "cute puppies",
        link: "pee.com",
        content: "poepoepoepoepoepoepoe"
      }, {
        id: 3,
        title: "cute pandas",
        link: "fart.com",
        content: "paepaepaepeapaepae"
      }]
    }
  }
}
</script>

<style>
#app {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

body {
  font-family: Arial, Helvetica, sans-serif;
  line-height: 1.4;
}

</style>
