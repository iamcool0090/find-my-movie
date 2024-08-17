<template>
    <div id="default-carousel" class="relative flex justify-center" data-carousel="slide">
        <div class="smaller-screen h-1/2 w-1/4 ">
            <!-- Carousel wrapper -->
            <div class="relative overflow-hidden rounded-lg md:h-screen">
                <!-- Item 1 -->
                <div class="duration-700 ease-in-out" :class="{ 'hidden': currentIndex !== 0 }">
                    <img :src="getImageSrc()"
                        class="absolute block w-full -translate-x-1/2 -translate-y-1/2 top-1/2 left-1/2" alt="...">
                </div>
                <!-- Item 2 -->
                <div class="duration-700 ease-in-out" :class="{ 'hidden': currentIndex !== 1 }">
                    <img :src="getImageSrc()"
                        class="absolute block w-full -translate-x-1/2 -translate-y-1/2 top-1/2 left-1/2" alt="...">
                </div>
                <!-- Item 3 -->
                <div class="duration-700 ease-in-out" :class="{ 'hidden': currentIndex !== 2 }">
                    <img :src="getImageSrc()"
                        class="absolute block w-full -translate-x-1/2 -translate-y-1/2 top-1/2 left-1/2" alt="...">
                </div>
                <!-- Item 4 -->
                <div class="duration-700 ease-in-out" :class="{ 'hidden': currentIndex !== 3 }">
                    <img :src="getImageSrc()"
                        class="absolute block w-full -translate-x-1/2 -translate-y-1/2 top-1/2 left-1/2" alt="...">
                </div>
                <!-- Item 5 -->
                <div class="duration-700 ease-in-out" :class="{ 'hidden': currentIndex !== 4 }">
                    <img :src="getImageSrc()"
                        class="absolute block w-full -translate-x-1/2 -translate-y-1/2 top-1/2 left-1/2" alt="...">
                </div>
            </div>
            <!-- Slider indicators -->
            <div class="absolute z-30 flex -translate-x-1/2 bottom-5 left-1/2 space-x-3 rtl:space-x-reverse">
                <button type="button" class="w-3 h-3 rounded-full" :class="{ 'bg-gray-800': currentIndex === 0 }"
                    aria-current="true" aria-label="Slide 1" @click="setCurrentIndex(0)"></button>
                <button type="button" class="w-3 h-3 rounded-full" :class="{ 'bg-gray-800': currentIndex === 1 }"
                    aria-current="false" aria-label="Slide 2" @click="setCurrentIndex(1)"></button>
                <button type="button" class="w-3 h-3 rounded-full" :class="{ 'bg-gray-800': currentIndex === 2 }"
                    aria-current="false" aria-label="Slide 3" @click="setCurrentIndex(2)"></button>
                <button type="button" class="w-3 h-3 rounded-full" :class="{ 'bg-gray-800': currentIndex === 3 }"
                    aria-current="false" aria-label="Slide 4" @click="setCurrentIndex(3)"></button>
                <button type="button" class="w-3 h-3 rounded-full" :class="{ 'bg-gray-800': currentIndex === 4 }"
                    aria-current="false" aria-label="Slide 5" @click="setCurrentIndex(4)"></button>
            </div>
            <!-- Slider controls -->
            <button type="button"
                class="absolute top-0 start-0 z-30 flex items-center justify-center h-full px-4 cursor-pointer group focus:outline-none"
                @click="prevSlide">
                <span
                    class="inline-flex items-center justify-center w-10 h-10 rounded-full bg-white/30 dark:bg-gray-800/30 group-hover:bg-white/50 dark:group-hover:bg-gray-800/60 group-focus:ring-4 group-focus:ring-white dark:group-focus:ring-gray-800/70 group-focus:outline-none">
                    <svg class="w-4 h-4 text-white dark:text-gray-800 rtl:rotate-180" aria-hidden="true"
                        xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 6 10">
                        <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                            d="M5 1 1 5l4 4" />
                    </svg>
                    <span class="sr-only">Previous</span>
                </span>
            </button>
            <button type="button"
                class="absolute top-0 end-0 z-30 flex items-center justify-center h-full px-4 cursor-pointer group focus:outline-none"
                @click="nextSlide">
                <span
                    class="inline-flex items-center justify-center w-10 h-10 rounded-full bg-white/30 dark:bg-gray-800/30 group-hover:bg-white/50 dark:group-hover:bg-gray-800/60 group-focus:ring-4 group-focus:ring-white dark:group-focus:ring-gray-800/70 group-focus:outline-none">
                    <svg class="w-4 h-4 text-white dark:text-gray-800 rtl:rotate-180" aria-hidden="true"
                        xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 6 10">
                        <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                            d="m1 9 4-4-4-4" />
                    </svg>
                    <span class="sr-only">Next</span>
                </span>
            </button>
        </div>
    </div>

</template>

<script>
export default {
    data() {
        return {
            maxImages: 200,
            currentIndex: 0
        };
    },
    methods: {
        getImageSrc() {
            const randomInteger = Math.floor(Math.random() * this.maxImages);
            return `http://localhost:8000/static/${randomInteger}.png`;
        },
        setCurrentIndex(index) {
            this.currentIndex = index;
        },
        prevSlide() {
            this.currentIndex = (this.currentIndex === 0) ? 4 : this.currentIndex - 1;
        },
        nextSlide() {
            this.currentIndex = (this.currentIndex === 4) ? 0 : this.currentIndex + 1;
        }
    }
};
</script>