<template>
    
    <div class="container">
        <b-card-group deck>
            <div v-for="article in articles" :key="article.id">
                <b-card :title="article.title" sub-title="Card subtitle">
                    <b-card-text>{{article.content}}</b-card-text>
                    <a :href="article.link" class="card-link">Full Story...</a>
                </b-card>
            </div>
        </b-card-group>
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