<template>
    <div id="app">
        <Buscas></Buscas> 
    </div>
</template>

<script>
import Buscas from './layouts/Buscas.vue'

export default {
    name: 'app',
    components: {
        Buscas
    }
}
</script>

<style lang="scss">
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }

    a {
        text-decoration: none;
    }
</style>
