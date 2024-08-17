<script setup>
import { RouterView } from 'vue-router';
import NavBar from './components/NavBar.vue';
import Footer from './components/Footer.vue';
</script>

<template>
  <div class="flex flex-col min-h-screen">
    <NavBar/>

    <div class="screen m-4 flex-grow">
      <RouterView/>
    </div>

    <Footer/>
  </div>
</template>

<style scoped>
.screen {
  /* Ensure the content area takes remaining height */
  flex-grow: 1;
}
</style>
