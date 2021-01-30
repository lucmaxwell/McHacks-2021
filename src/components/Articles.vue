<template>
    
    <div>
        <p>can I see this</p>
        <div>
            <p>testing</p>
            
        </div>
        <p>poopoo</p>
        <div v-for="article in articles" :key="article.id">
            <h3>{{article.title}}</h3>
            <p>poop</p>
        </div>
    </div>

    
</template>
<script>
export default {
    name: "Articles" ,
    props: ["articles"]  
}
</script>
<style scoped>

</style>