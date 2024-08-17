<script setup>
import Card from '@/components/Card.vue';
</script>

<template>
    <div v-if="!showSearchResults" class="vh-100">
        <label for="default-search"
            class="mb-2 text-sm font-medium text-gray-900 sr-only dark:text-white">Search</label>
        <div class="relative">
            <div class="absolute inset-y-0 start-0 flex items-center ps-3 pointer-events-none">
                <svg class="w-4 h-4 text-gray-500 dark:text-gray-400" aria-hidden="true"
                    xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 20 20">
                    <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                        d="m19 19-4-4m0-7A7 7 0 1 1 1 8a7 7 0 0 1 14 0Z" />
                </svg>
            </div>
            <input type="search" id="default-search"
                class="block w-full p-4 ps-10 text-sm text-gray-900 border border-gray-300 rounded-lg bg-gray-50 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                placeholder="Find Your Movies with Natural Language" required />
            <button @click="search"
                class="text-white absolute end-2.5 bottom-2.5 bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-4 py-2 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">Search</button>
        </div>
        <div class="text-art gap-4 mt-4">
            <h1 class="text-4xl font-bold text-center">Welcome to find-that-movie.com</h1>
            <br />
            <p class="text-center">Discover movies like never before. Our simple and intuitive movie app allows you to
                search for films by entering their descriptions. </p>
        </div>
    </div>
    <div v-else>
        <div class="p-4">
            <p class="text-lg">Showing Results for: <b>{{ searchQuery }}</b></p>
            <a href="/" class="text-blue-500">&lt;- Go Back</a>
            <div v-if="movies" class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4 mt-4">
                <Card v-for="movie in movies" :key="movie.id" :movie="movie" />
            </div>
        </div>

    </div>
</template>


<script>
import axios from 'axios';

export default {
    data() {
        return {
            movies: [],
            showSearchResults: false,
            searchQuery: ''
        };
    },
    methods: {
        async search() {
            let response = await axios.post('http://localhost:8000/api/movies/natural-language', {
                text: document.getElementById('default-search').value
            });

            this.movies = response.data;
            this.showSearchResults = true;
            this.searchQuery = document.getElementById('default-search').value;

        }
    }
};
</script>
