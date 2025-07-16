<template>
  <section class="home-page">
    <AddTasks />
    <TodoTable />
  </section>
</template>

<script setup lang="ts">
// local registration to compoment ts
import AddTasks from '@/components/AddTasks.vue'
import TodoTable from '@/components/TodoTable.vue'
</script>
<style>
.home-page {
  min-width: 500px;
  width: 60%;
  min-height: 200px;
  height: 50%;
  max-height: 500px;
  /* background-color: red; */
}
</style>
