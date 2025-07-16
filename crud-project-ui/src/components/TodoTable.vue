<template>
  <section class="table-section">
    <div v-if="loading">Loading...</div>
    <div v-else-if="error">{{ error }}</div>
    <div v-else>
      <ul>
        <li v-for="item in todoItems" :key="item.id">
          {{ item.task }} - {{ item.task_status }}
          <span class="description" v-if="item.description">({{ item.description }})</span>
        </li>
      </ul>
    </div>
  </section>
</template>

<script lang="ts" setup>
import { ref, onMounted } from 'vue'

interface TodoItem {
  id: number
  task: string
  description: string
  task_status: string
}

const todoItems = ref<TodoItem[]>([])
const loading = ref(true)
const error = ref<string | null>(null)

onMounted(async () => {
  try {
    const response = await fetch('http://127.0.0.1:8000/tasks/')

    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`)
    }

    const data: TodoItem[] = await response.json()
    console.log('API Response:', data)

    // Validate data structure
    if (!Array.isArray(data)) {
      throw new Error('Expected array but received different data structure')
    }

    todoItems.value = data.map((item) => ({
      id: item.id,
      task: item.task || 'No task',
      description: item.description || '',
      task_status: item.task_status || 'unknown',
    }))
  } catch (err) {
    error.value = err instanceof Error ? err.message : 'Failed to fetch data'
    console.error('Fetch error:', err)
  } finally {
    loading.value = false
  }
})
</script>

<style>
.table-section {
  padding: 20px;
  font-family: Arial, sans-serif;
  max-width: 800px;
  margin: 0 auto;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  padding: 12px 16px;
  margin: 8px 0;
  background: #f5f5f5;
  border-radius: 6px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.description {
  color: #666;
  font-size: 0.9em;
  margin-left: 10px;
}
</style>
