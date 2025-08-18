<template>
  <block-ab title="Теперь мы в ''Профессионалитете''!">
    <div class="img-container">
      <div class="slider">
        <div class="slider-track" :style="{ transform: `translateX(-${currentIndex * 100}%)` }">
          <div class="slide" v-for="(image, index) in images" :key="index">
            <img class="slider-image" :src="image" alt="Фото" />
          </div>
        </div>
        <button class="slider-button prev" @click="prevSlide">‹</button>
        <button class="slider-button next" @click="nextSlide">›</button>
      </div>
    </div>
    <div class="video-container">
      <video class="ab__video" controls>
        <source src="/video/Профессионалитет Видео.mp4" type="video/mp4" />
        Ваш браузер не поддерживает видео
      </video>
    </div>
    <p class="ab__p" style="margin: auto">
      2 сентября 2024 на базе Колледжа инновационных технологий, экономики и коммерции в рамках Дня
      знаний состоялось торжественное открытие образовательного кластера "Союз +" в отрасли «Туризм
      и сфера услуг» Федерального проекта «Профессионалитет». Федеральный проект «Профессионалитет»
      – это современные направления развития среднего профессионального образования, которые
      предполагают открытие новых учебно-производственных площадок по видам деятельности, оснащенных
      современным оборудованием и предлагает обучение множеству интересных и разнообразных
      специальностей. «Профессионалитет» - дает выпускникам гарантии трудоустройства, укрепляет
      связи с работодателями, предоставляет возможность каждому студенту отработать навыки
      профессионального мастерства в современных лабораториях в более сжатые сроки
      практико-ориентированного обучения.
    </p>
    <div class="video-container">
      <video class="ab__video" controls>
        <source src="/video/ВИДЕО КЛАСТЕР СОЮЗ +.mp4" type="video/mp4" />
        Ваш браузер не поддерживает видео
      </video>
    </div>
  </block-ab>
</template>

<script>
export default {
  data() {
    return {
      images: [
        '/img/student-professionalitet/photo/1.webp',
        '/img/student-professionalitet/photo/2.webp',
        '/img/student-professionalitet/photo/3.webp',
        '/img/student-professionalitet/photo/4.webp',
        '/img/student-professionalitet/photo/5.webp',
        '/img/student-professionalitet/photo/6.webp',
        '/img/student-professionalitet/photo/7.webp',
        '/img/student-professionalitet/photo/8.webp',
        '/img/student-professionalitet/photo/9.webp',
        '/img/student-professionalitet/photo/10.webp',
        '/img/student-professionalitet/photo/11.webp',
        '/img/student-professionalitet/photo/12.webp',
        '/img/student-professionalitet/photo/13.webp',
        '/img/student-professionalitet/photo/14.webp',
        '/img/student-professionalitet/photo/15.webp',
        '/img/student-professionalitet/photo/16.webp',
        '/img/student-professionalitet/photo/22.webp',
        '/img/student-professionalitet/photo/23.webp',

        // Добавьте остальные пути к изображениям
      ],
      currentIndex: 0,
    }
  },
  methods: {
    nextSlide() {
      if (this.currentIndex < this.images.length - 1) {
        this.currentIndex++
      } else {
        this.currentIndex = 0 // Возвращаемся к первому слайду
      }
    },
    prevSlide() {
      if (this.currentIndex > 0) {
        this.currentIndex--
      } else {
        this.currentIndex = this.images.length - 1 // Переходим к последнему слайду
      }
    },
  },
}
</script>

<style scoped lang="scss">
.ab {
  &__video {
    width: 100%;
    max-width: 580px;
    border-radius: 15px;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.15);
    margin: 20px auto;
    display: block;

    @include small-media() {
      max-width: 260px;
    }
  }
}

.img-container {
  .slider {
    position: relative;
    width: 100%;
    max-width: 580px;
    margin: 20px auto;
    overflow: hidden;
    border-radius: 15px;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.15);

    .slider-track {
      display: flex;
      transition: transform 0.5s ease-in-out;
    }

    .slide {
      min-width: 100%;
      box-sizing: border-box;

      .slider-image {
        width: 100%;
        height: auto;
        object-fit: cover;
        border-radius: 15px;
      }
    }

    .slider-button {
      position: absolute;
      top: 50%;
      transform: translateY(-50%);
      background: rgba(255, 255, 255, 0.7);
      border: none;
      color: #333;
      padding: 10px 15px;
      cursor: pointer;
      z-index: 10;
      transition: background 0.3s;

      &:hover {
        background: rgba(255, 255, 255, 1);
      }
    }

    .prev {
      left: 10px;
    }

    .next {
      right: 10px;
    }
  }
}

.video-container {
  max-width: 580px;
  margin: 20px auto;
  border-radius: 15px;
  overflow: hidden;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.15);
  display: flex;
  justify-content: center;
}

/* Адаптивность */
@media (max-width: 768px) {
  .img-container .slider,
  .video-container {
    max-width: 100%;
  }

  .img-container .slider-button {
    padding: 8px 12px;
  }
}
</style>
