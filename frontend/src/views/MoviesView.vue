<script setup>
import { ref, onMounted, watch } from 'vue';
import { useRoute } from 'vue-router';
import Card from '@/components/Card.vue';
import axios from 'axios';

const movies = ref([]);
const route = useRoute();
const language = ref(route.params.language);

const fetchMovies = async (language) => {
  try {
    const response = await axios.get(`http://localhost:8000/api/movies/${language}`);
    if(response.data.length == 0){
        movies.value = null;
    }else{
        movies.value = response.data;
    }
  } catch (error) {
    console.error('Error fetching movies:', error);
  }
};

onMounted(() => {
  fetchMovies(language.value);
});

watch(() => route.params.language, (newLanguage) => {
  language.value = newLanguage;
  fetchMovies(newLanguage);
});

</script>

<template>
  <div v-if="movies" class="grid grid-cols-1 sm:grid-cols-3 sm:grid-cols-3 lg:grid-cols-4  gap-4">
    <Card v-for="movie in movies" :key="movie.id" :movie="movie" />
  </div>
  <div v-else>
    <section class="bg-white dark:bg-gray-900 ">
        <div class="container flex items-center min-h-3.5 px-6 py-6 mx-auto">
            <div class="flex flex-col items-center max-w-sm mx-auto text-center">
                <p class="p-3 text-sm font-medium text-blue-500 rounded-full bg-blue-50 dark:bg-gray-800">
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" class="w-6 h-6">
                        <path stroke-linecap="round" stroke-linejoin="round" d="M12 9v3.75m9-.75a9 9 0 11-18 0 9 9 0 0118 0zm-9 3.75h.008v.008H12v-.008z" />
                    </svg>
                </p>
                <h1 class="mt-3 text-2xl font-semibold text-gray-800 dark:text-white md:text-3xl">Page not found</h1>
                <p class="mt-4 text-gray-500 dark:text-gray-400">The page you are looking for doesn't exist. Here are some helpful links:</p>
            </div>
        </div>
    </section>
  </div>
</template>
