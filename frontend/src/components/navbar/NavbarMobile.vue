<script setup lang="ts">
import { defineComponent, ref } from 'vue';

import Button from 'primevue/button';
import Drawer from 'primevue/drawer';

defineComponent({
  name: 'NavbarMobile',
})

const showDrawer = ref(false);

</script>


<template>

  <Button icon="pi pi-bars" @click="showDrawer = true" />

  <Drawer v-model:visible="showDrawer" header="Drawer">
      <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</p>
  </Drawer>
  
</template>
