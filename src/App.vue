<template>
  <div id="app">
    <Header/>
    <Articles :articles="articles"/>
  </div>

  
</template>

<script>
import Header from './components/Header';
import Articles from './components/Articles';

var info;
var i;
const axios = require('axios');

//const proxyurl = "https://cors-anywhere.herokuapp.com/";
//const url = 'http://127.0.0.1:5000';

function myFunction(){
  axios.get('http://127.0.0.1:5000',{
  }).then(resp => {

    info = (resp.data);
    //data = JSON.parse(data);
    info = info.message;
    info = info.toString();
    info = info.split('\n\n\n\n');
    for (i=0; i< info.length; i++){
      info[i] = info[i].split('\n\n\n');
    }
    info.forEach(element => console.log(element))
    return info;
  
  });
  

}
var list = myFunction();
console.log(list);
var articles = [];
var person;
for (i=0; i<articles.length;i++ ){
  person = new Object();
  person.id = list[i][0];
  person.link = list[i][3];
  person.title = list[i][1];
  person.content = list[i][2];
  articles.push(person);
}

export default {
  name: 'App',
  components: {
    Header,
    Articles
   
  },
  data(){
    return {
      articles: [{
        id: 0,
        title: "Wynton Marsalis on segregation, jazzocracy and activism through instrumental music",
        link: "https://cbc.ca/radio/q/monday-jan-25-2021-wynton-m…and-activism-through-instrumental-music-1.5886220",
        content: "Wynton Marsalis has been at the forefront of jazz …rica's then-newly inaugurated President Obama...."

      },{
        id: 1,
        title: "For these people, Donald Trump's defeat may have changed their lives",
        link: "https://cbc.ca/news/world/daca-minors-immigration-trump-1.5893320",
        content: "Few people were more deeply, personally, emotional…an a group commonly referred to as 'Dreamers.'..."
      }, {
        id: 2,
        title: "Nigeria: the country that loves to overachieve",
        link: "https://www.bbc.com/travel/story/20210124-nigeria-the-country-that-loves-to-overachieve",
        content: "In a lifetime of feverishly competitive Scrabble-p… as natural as spicy jollof rice at a wedding...."
      },{
        id: 5,
        title:"Edmonton antique hunter finds unexpected grand treasures in piano teacher's estate",
        content:"It was the grand piano that convinced Edmonton ant…chase Bette-Joan Rac's estate after her death....",
        link:"https://cbc.ca/news/canada/edmonton/antique-hunter-treasure-piano-teacher-estate-1.5893876"
      },{
        id: 6,
        title: "Treats, water fights and rockets — 5 Asian holidays that’ll make you want to celebrate!",
        content:"Treats, water fights and rockets — 5 Asian holidays that’ll make you want to celebrate!...",
        link:"https://www.cbc.ca/kidscbc2/the-feed/treats-water-…ckets-five-asian-holidays-make-you-want-celebrate"
      },{
        id: 7,
        title:"Old meets new on Black Alliance, Vol. 1, a set of 6 cover songs by Jacksoul, Amaal, Just John and more",
        content: "Just days before the start of Black History Month, Warner Music Canada has released Black Alliance, Vol. 1, a collection of six songs by legendary Black artists, covered by Canadians — including the posthumous track 'Use Me,' a Bill Withers classic sung by the late Haydain Neale of Jacksoul fame....",
        link: "https://cbc.ca/music/old-meets-new-on-black-alliance-vol-1-a-set-of-6-cover-songs-by-jacksoul-amaal-just-john-and-more-1.5893445"
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
