import { defineStore } from "pinia";
import { ref } from "vue";


export const useScreenStore = defineStore('screen', () => {

  const screenWidth = ref(window.innerWidth);

  const getScreenWidth = () => screenWidth.value;

  const updateScreenWidth = () => {

    screenWidth.value = window.innerWidth;
  }

  return {
    getScreenWidth,
    updateScreenWidth
  }

})