import { ref } from "vue";
import { defineStore } from "pinia";


export const useTaskStore = defineStore('task', () => {

  const valuesUpdated = ref(false);

  const updatedValues = (value: boolean) => {
    valuesUpdated.value = value;
  }

  const getValuesUpdated = () => {
    return valuesUpdated.value;
  }

  return {
    getValuesUpdated,
    updatedValues
  }

});
