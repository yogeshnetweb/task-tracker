<template>
  <section class="add-task-section">
    <input type="text" id="input-field" />
    <button id="submit-btn">Add Task</button>
  </section>
</template>

<script lang="ts" setup></script>

<style>
.add-task-section {
  width: 100%;
  height: 100%;
  display: flex;
  gap: 1rem;
}

#input-field {
  flex: 3;
  padding: var(--padding);
  font-family: var(--font-family);
  font-size: var(--font-size);
}

#submit-btn {
  flex: 1;
  padding: var(--padding);
  font-family: var(--font-family);
  font-size: var(--font-size);
}
</style>
