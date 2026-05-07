<script setup lang="ts">
import { computed } from 'vue';

import { RouterView } from 'vue-router'

import { useUserStore } from './stores/user';

import Toast from 'primevue/toast';
import NavbarDesktop from './components/navbar/NavbarDesktop.vue';
import LoginCadForm from './components/modal/LoginCadForm.vue';

const { userLoggedIn } = useUserStore();

const user = computed(() => userLoggedIn());

</script>

<template>

  <Toast position="bottom-center"/>

  <LoginCadForm v-if="!user"/>

  <div class="flex flex-row">

    <NavbarDesktop/>

    <main v-if="user">
      <RouterView />
    </main>
  </div>

</template>

<style scoped>

main {
  margin-top: 5rem;
  margin-left: 25rem;
  width: 100%;
}

</style>
