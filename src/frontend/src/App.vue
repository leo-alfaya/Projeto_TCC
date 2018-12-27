<template>
  <div id="app">
      <el-container>
        <el-header></el-header>
        <el-main>
            <Buscas></Buscas> 
        </el-main>
      </el-container>
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
</style>
