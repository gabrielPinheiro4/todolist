import { ref } from "vue";
import { defineStore } from "pinia";


export const useTaskStore = defineStore('task', () => {

  const taskAdded = ref(false);

  const updateTaskAdded = (value: boolean) => {
    taskAdded.value = value;
  }

  const getTaskAdded = () => {
    return taskAdded.value;
  }

  return {
    getTaskAdded,
    updateTaskAdded
  }

});
