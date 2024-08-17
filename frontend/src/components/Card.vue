<template>
    <div class="max-w-sm bg-white border border-gray-200 rounded-lg shadow-md dark:bg-gray-800 dark:border-gray-700 overflow-hidden">
      <div class="image-holder">

        <img class="w-full h-48 object-cover" :src="`http://localhost:8000/static/${movie[5]}`" alt="Movie Thumbnail" />
      </div>
      <div class="p-5">
        <a href="#">
          <h5 class="mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white">{{ movie[1] }}</h5>
        </a>
        <b class="block mb-3 text-gray-800 dark:text-gray-300">
          {{ movie[3] }}<br/>
          Ratings: {{ movie[6] }}<br /> Votes: {{ movie[7] }}
        </b>

        <div class="scrollable-text-window max-h-24 overflow-y-auto">
          <p class="mb-3 font-normal text-gray-700 dark:text-gray-400">{{ movie[4] }}</p>
        </div>
      </div>
    </div>
  </template>
  


<style>
.image-holder {
    position: relative;
    overflow: hidden;
    border-radius: 0.5rem 0.5rem 0 0;
    height: 200px;
}

.scrollable-text-window{
  width: 300px; /* Set the width of the text window */
  height: 150px; /* Set the height of the text window */
  overflow-y: auto; /* Make the text window scrollable */

}

.scrollable-text-window::-webkit-scrollbar {
  display: none;
}

</style>

<script>

export default {
    props: {
        movie: {
            type: Array,
            required: true
        }
    },
    computed: {
        truncatedDescription(description) {
            const maxLength = 100; // Set the max length for the description
            if (description > maxLength) {
                return description.substring(0, maxLength) + '...';
            }
            return description;
        }
    }
}


</script>