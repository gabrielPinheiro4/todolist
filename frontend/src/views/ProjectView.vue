<script setup lang="ts">

import { useTaskStore } from '@/stores/task';
import { useToast } from 'primevue';
import { useRoute } from 'vue-router';
import { computed, onMounted, ref, watch } from 'vue';

import Project from '@/models/Project';

import Select from 'primevue/select';
import DatePicker from 'primevue/datepicker';
import InputText from 'primevue/inputtext';
import Dialog from 'primevue/dialog';
import Button from 'primevue/button';
import Message from 'primevue/message';

import Priority from '@/models/Priority';
import Status from '@/models/Status';

import type {
  ProjectInterface, StatusPriorityInterface, TaskInterface
} from '@/types/env';


import Task from '@/models/Task';
import { isAxiosError } from 'axios';

const route = useRoute();

const { add } = useToast();

const { getValuesUpdated, updatedValues } = useTaskStore();

const taskAddedValue = computed(() => getValuesUpdated())

const showModalTask = ref(false);

const formDiferent = computed(() => {

  return (
      formEditTask.value.title && (
        formEditTask.value.title
        .toLowerCase().trim() !== taskSelected.value?.title.toLowerCase().trim()
      )

    || formEditTask.value.desc && (
      formEditTask.value.desc
      .toLowerCase().trim() !== taskSelected.value?.desc.toLowerCase().trim()
    )

    || formEditTask.value.priority.title !== taskSelected.value?.priority.title
    || formEditTask.value.status.title !== taskSelected.value?.status.title

    || formEditTask.value.dateExpiration
    .toLocaleDateString('pt-BR') !== new Date(
      taskSelected.value.dateExpiration.split('00:00:00 GMT')[0] as string
    ).toLocaleDateString('pt-BR')
  )
});

const taskSelected = ref<TaskInterface | null>(null);

const projectSelected = ref<ProjectInterface | null>(null);

const allPriorities = ref<StatusPriorityInterface[] | null>(null);

const allStatus = ref<StatusPriorityInterface[] | null>(null);

const projectIDParam = computed(
  () => route.params.id as string
);

const formEditTask = ref({
  title: '',
  desc: '',
  dateExpiration: new Date(),
  priority: {} as StatusPriorityInterface,
  status: {} as StatusPriorityInterface

});

const openModalTask = (task: TaskInterface) => {
  taskSelected.value = task;
  showModalTask.value = true;
}

const editTask = async () => {

  if (taskSelected.value) {

    const res = await Task.editTask(
      taskSelected.value.id,
      formEditTask.value.title,
      formEditTask.value.desc,
      formEditTask.value.priority.id,
      formEditTask.value.status.id,
      formEditTask.value.dateExpiration,
    );

    if (res) {
      add({
        severity: 'success',
        summary: 'Sucesso',
        detail: res,
        life: 4000
      });

      await updateProjectValue(projectIDParam.value);

      showModalTask.value = false;
    }
  }
}

const delTask = async () => {

  try {

    if (taskSelected.value) {

      const res = await Task.delTask(taskSelected.value.id);

      if (res) {

        add({
          severity: 'success',
          summary: 'Sucesso',
          detail: res,
          life: 4000
        });

        showModalTask.value = false;

        updatedValues(true);
      }
    }
  } catch (error) {

    if (isAxiosError(error)) {

      add({
        severity: 'error',
        summary: 'Error',
        detail: error,
        life: 4000
      });
    }
  }

}

const updateProjectValue = async (id: string) => {

  console.log('a')

  const project = await Project.getProjects(id);

  if (project && !(project instanceof Array)) {
    projectSelected.value = project;
  }
}

watch(
  [projectIDParam, taskSelected, taskAddedValue],
  async ([newID, newTask, newAdded], [_, oldTask]

  ) => {

  if (newAdded) {

    await updateProjectValue(newID);

    updatedValues(false);
  }

  await updateProjectValue(newID);

  if (newTask && newTask != oldTask) {

    formEditTask.value.title = newTask.title;

    formEditTask.value.desc = newTask.desc;

    formEditTask.value.dateExpiration = new Date(

      newTask.dateExpiration.split('00:00:00 GMT')[0] as string
    );

    formEditTask.value.priority = newTask.priority;

    formEditTask.value.status = newTask.status;
  }

}, { immediate: true });

onMounted(async () => {
  const priorities = await Priority.getPriorities();

  const status = await Status.getStatus();

  if (priorities && status) {
    allPriorities.value = priorities;
    allStatus.value = status;
  }
});

</script>

<template>

  <Dialog
    v-if="projectSelected"
    v-model:visible="showModalTask"
    modal
    position="top"
    :draggable="false"
    :header="`#${projectSelected.title}`"
    :style="{ width: '40rem' }">

    <div class="flex flex-col">

      <div
        :style="{width: '100%'}"
        class="modal-items flex flex-row justify-between gap-1">

        <div class="flex flex-col">

          <InputText
            :style="{ paddingBottom: '0', paddingLeft: '0' }"
            class="new-task-input task-bold"
            type="text"
            v-model="formEditTask.title" />

          <InputText
            :style="{ paddingLeft: '0' }"
            size="small"
            class="new-task-input"
            type="text"
            placeholder="Descrição"
            v-model="formEditTask.desc" />
        </div>

        <div class="flex flex-col gap-2 right-side">

          <div class="flex flex-col gap-1">
            
            <Message size="small" severity="secondary" variant="simple">
              Data de vencimento
            </Message>

            <DatePicker
              class="date-expiration-task"
              :style="{width: '8rem'}"
              v-model="formEditTask.dateExpiration"
              dateFormat="dd/mm/yy"
              size="small"
              showIcon
              fluid
              iconDisplay="input"
              inputId="icondisplay" />
          </div>

          <div class="flex flex-col gap-1">

            <Message size="small" severity="secondary" variant="simple">
              Prioridade
            </Message>

            <Select
              v-if="allPriorities"
              size="small"
              v-model="formEditTask.priority"
              :options="allPriorities"
              optionLabel="title"
              class="w-full" />

          </div>

          <div class="flex flex-col gap-1">

            <Message size="small" severity="secondary" variant="simple">
              Status
            </Message>

            <Select
              v-if="allStatus"
              size="small"
              v-model="formEditTask.status"
              :options="allStatus"
              optionLabel="title"
              class="w-full" />

          </div>

        </div>

      </div>

      <div class="btns-task flex flex-row gap-2">

        <Button
          size="small"
          type="button"
          label="Cancelar"
          severity="secondary"
          @click="showModalTask = false" />

        <Button
          size="small"
          type="button"
          label="Editar tarefa"
          :disabled="!formDiferent"
          @click="editTask" />

          <Button
            size="small"
            type="button"
            severity="danger"
            label="Deletar tarefa"
            @click="delTask" />
      </div>
    </div>
  </Dialog>

  <section class="project-view" v-if="projectSelected">

    <div class="flex flex-col gap-1">
      <h2 class="font-bold">{{ projectSelected.title }}</h2>

      <Message size="small" severity="secondary" variant="simple">
        {{ projectSelected.desc }} -
        {{ new Date(projectSelected.dateCreation).toLocaleDateString('pt-BR') }}
      </Message>
    </div>

    <div
      v-if="projectSelected.tasks.length > 0"
      class="tasks flex flex-col gap-3">

      <div
        @click="openModalTask(task)"
        v-for="task in projectSelected.tasks"
        :key="task.id">

        <div class="flex flex-col gap-1 open-modal-task">

          <div class="flex flex-row items-center gap-2">
            <div class="circle"></div>
            <p class="title-task font-bold">{{ task.title }}</p>
          </div>

          <Message size="small" severity="secondary" variant="simple">
            {{ task.desc }}
          </Message>

          <Message size="small" severity="secondary" variant="simple">
            Expira em {{ new Date(task.dateExpiration).toLocaleDateString('pt-BR', {timeZone: 'UTC'}) }}
          </Message>

        </div>

      </div>
    </div>

    <p v-else class="mt-3" :style="{color: '#f97316'}">
      Esse projeto não possui nenhuma tarefa
    </p>

  </section>
</template>

<style scoped>

h2 {
  font-size: 1.7rem;
}

.circle {
  background: #f97316;
  border-radius: 100%;
  width: 5px;
  height: 5px;
}

.tasks {
  margin-top: 2rem;
}

.title-task {
  font-size: 1.2rem;
}

.open-modal-task {
  cursor: pointer;
}

@media (max-width: 572px) {
  .btns-task {
    margin-top: 2rem;
  }

  .modal-items {
    flex-direction: column;
  }

  .date-expiration-task {
    width: 100% !important;
  }

  .right-side {
    margin-top: 1rem;
  }
}

</style>
