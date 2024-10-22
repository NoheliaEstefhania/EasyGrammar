<script setup>
import App1 from './components/App1.vue'
</script>

<template>
  <header class="flex flex-row justify-between p-6">
    <div class="">
      <!-- Logo img here -->
      <h1 class="text-3xl font-bold">遊 WordWeaver</h1>
    </div>
    <div class="flex flex-row gap-3">
      <button>
        <img class="w-8" src="./assets/icons/notification-icon.svg" alt="notification">
      </button>
      <button>
        <img class="w-8" src="./assets/icons/user-icon.svg" alt="notification">
      </button>
    </div>
  </header>
  <!-- Convert to component -->
  
  <main class="px-14 py-10">
    <App1/>
  </main>

  





  <!-- Background Images -->
  <img src="./assets/imgs/sun-img.png" class="absolute top-0 left-0 -z-10"   alt="leaft">
  <img src="./assets/imgs/leaf2left.png" class="absolute bottom-0 left-0 -z-10" alt="leaft">
  <img src="./assets/imgs/leaf1Left.png"  class="absolute bottom-0 left-0 -z-10" alt="leaft">
  <img src="./assets/imgs/leafRight3.png" class="absolute right-0 top-14 -z-10"  alt="leaft">
  <img src="./assets/imgs/leafRight2.png" class="absolute bottom-0 right-0 -z-10"  alt="leaft">
  <img src="./assets/imgs/leafRight1.png" class="absolute bottom-0 right-0 -z-10"  alt="leaft">
  <img src="./assets/imgs/leafRight4.png" class="absolute right-0 top-64 -z-10"  alt="leaft">
 
</template>
<style scoped>
</style>
 