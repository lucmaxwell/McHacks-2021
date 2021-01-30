<template>
  <div id="app">
    <p>poopoo</p>
    <Header/>
    <Articles :articles="articles"/>
  </div>

  
</template>

<script>
import Header from './components/Header';
import Articles from './components/Articles';




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
        link: "poop.com"

      },{
        id: 2,
        title: "cute puppies",
        link: "pee.com"
      }, {
        id: 3,
        title: "cute pandas",
        link: "fart.com"
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
