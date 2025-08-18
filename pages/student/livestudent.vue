<template>
  <block-ab title="Студенческая жизнь: открывай мир, твори будущее!">
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
    <div class="slider-text" v-if="currentIndex === 0">
      <p class="ab__pp">
        Заместитель Министра образования Омской области Анатолий Сергеевич Полынский поздравляет
        студентов первого и второго курсов, поступивших в колледж на специальности <br />ФП
        «Профессионалитет» 02.09.2024.
      </p>
    </div>
    <div class="slider-text" v-if="currentIndex === 1">
      <p class="ab__pp">
        Амбассадоры Профессионалитета, студенты 2 курса специальности «Туризм и гостеприимство»
        Матвей и Варвара на экскурсии в туристическом объекте «Дендросад»
      </p>
    </div>
    <div class="slider-text" v-if="currentIndex === 2">
      <p class="ab__pp">
        Студентов поздравляют с началом нового учебного года 02 сентября 2024 года: Омский
        предприниматель, ресторатор, соучредитель известных в Омске заведений: ресторан "Где же
        Кролик"; Friendly bar "АбсентоМоре"; Шоу-бар "Кукла"; Караоке бар "Опера"; Мясо-бар "Корова
        на бочке"; Кальян-бар "SmokyDock"; "Double bubble tea", резидент федерального клуба
        предпринимателей "Эталон", наставник в программе для предпринимателей по масштабированию
        бизнеса ScaleUp <b>Василий Алексеевич Хомицкий</b> И Директор Обществ с ограниченной
        ответственностью «ВЕРСИЯ» и «СИБКОР-2», совладелец ресторана «Сенкевич», учредитель Общества
        с ограниченной ответственностью «Музыка и кино», ресторатор в группе предприятий, включающей
        сеть кафе-бистро «Курочка рядом», торгово-развлекательный комплекс «Кристалл»,
        развлекательный комплекс «Топаз», рестораны «Арена», «Радио Сибирь», знаток и ценитель
        кулинарного искусства, коуч и наставник — <b>Павел Юрьевич Щелконогов</b>.
      </p>
    </div>
    <div class="slider-text" v-if="currentIndex === 3">
      <p class="ab__pp">
        Студенты 2 курса специальности "Информационные системы и программирование" знакомятся со
        средой программирования Visual Studio на учебном занятии по дисциплине <br />
        "Основы алгоритмизации и программирования"
      </p>
    </div>
    <div class="slider-text" v-if="currentIndex === 4">
      <p class="ab__pp">
        Студенты 3 курса специальности "Поварское и кондитерское дело" производят сервировку чайного
        стола и складывание салфеток различной формы на учебном занятии по дисциплине "Организация
        обслуживания"
      </p>
    </div>
    <div class="slider-text" v-if="currentIndex === 5">
      <p class="ab__pp">
        Студенты 2 курса специальности "Информационные системы и программирование" изучают парадигмы
        языков программирования на учебном занятии по дисциплине "Основы алгоритмизации и
        программирования"
      </p>
    </div>
    <div class="slider-text" v-if="currentIndex === 6">
      <p class="ab__pp">
        Студенты 3 курса специальности "Поварское и кондитерское дело" производят сервировку чайного
        стола и складывание салфеток различной формы на учебном занятии по дисциплине "Организация
        обслуживания"
      </p>
    </div>
    <div class="slider-text" v-if="currentIndex === 7">
      <p class="ab__pp">
        Студенты 3 курса специальности "Поварское и кондитерское дело" производят сервировку чайного
        стола и складывание салфеток различной формы на учебном занятии по дисциплине "Организация
        обслуживания"
      </p>
    </div>
    <div class="slider-text" v-if="currentIndex === 8">
      <p class="ab__pp">
        Студенты 2 курса специальности "Информационные системы и программирование" знакомятся со
        средой программирования Visual Studio на учебном занятии по дисциплине "Основы
        алгоритмизации и программирования"
      </p>
    </div>
    <div class="slider-text" v-if="currentIndex === 9">
      <p class="ab__pp">
        Студенты 2 курса специальности "Туризм и гостеприимство" направленности "гостиничные услуги"
        отрабатывают технику общения с гостем в процессе информирования о достопримечательностях г.
        Омска <br />в рамках учебного занятия по <br />МДК.01.01. Координация работы служб
        предприятий туризма и гостеприимства
      </p>
    </div>
    <div class="slider-text" v-if="currentIndex === 10">
      <p class="ab__pp">
        Студенты 2 курса специальности "Туризм и гостеприимство" направленности "гостиничные услуги"
        изучают правила обслуживания в гостиницах и иных средствах размещения на учебном занятии по
        МДК.01.01. <br />Координация работы служб предприятий туризма и гостеприимства
      </p>
    </div>
    <div class="slider-text" v-if="currentIndex === 11">
      <p class="ab__pp">
        Студенты 2 курса специальности "Туризм и гостеприимство" направленности "гостиничные услуги"
        анализируют рынок гостиничного продукта в регионе, проводят оценку деятельности гостиничных
        предприятий по заданным показателям
      </p>
    </div>
    <div class="slider-text" v-if="currentIndex === 12">
      <p class="ab__pp">
        Студенты осмысливают роль и место знаний по МДК.01.01 Координация работы служб предприятий
        туризма и гостеприимства в процессе освоения образовательной программы по специальности
        <br />
        "Туризм и гостеприимство" направленности "гостиничные услуги"
      </p>
    </div>
    <div class="slider-text" v-if="currentIndex === 13">
      <p class="ab__pp">
        Студенты 2 курса специальности "Туризм и гостеприимство" направленности "гостиничные услуги"
        отрабатывают технику общения с гостем в процессе информирования о достопримечательностях г.
        Омска в рамках учебного занятия по МДК.01.01. Координация работы служб предприятий туризма и
        гостеприимства
      </p>
    </div>
    <div class="slider-text" v-if="currentIndex === 14">
      <p class="ab__pp">
        Студенты 2 курса специальности "Туризм и гостеприимство" направленности "гостиничные услуги"
        анализируют рынок гостиничного продукта в регионе, проводят оценку деятельности гостиничных
        предприятий по заданным показателям
      </p>
    </div>
    <div class="slider-text" v-if="currentIndex === 15">
      <p class="ab__pp">
        Студенты осмысливают роль и место знаний по МДК.01.01 Координация работы служб предприятий
        туризма и гостеприимства в процессе освоения образовательной программы по специальности
        <br />
        "Туризм и гостеприимство" направленности "гостиничные услуги"
      </p>
    </div>
    <div class="slider-text" v-if="currentIndex === 16">
      <p class="ab__pp">
        Студент 3 курса специальности "Поварское и кондитерское дело" сортирует столовую посуду для
        организации рабочего места бармена на учебном занятии по дисциплине "Организация
        обслуживания"
      </p>
    </div>
  </block-ab>
</template>

<script>
export default {
  data() {
    return {
      images: [
        '/img/live-student/1.webp',
        '/img/live-student/2.webp',
        '/img/live-student/3.webp',
        '/img/live-student/4.webp',
        '/img/live-student/5.webp',
        '/img/live-student/6.webp',
        '/img/live-student/7.webp',
        '/img/live-student/8.webp',
        '/img/live-student/9.webp',
        '/img/live-student/10.webp',
        '/img/live-student/11.webp',
        '/img/live-student/12.webp',
        '/img/live-student/13.webp',
        '/img/live-student/14.webp',
        '/img/live-student/15.webp',
        '/img/live-student/16.webp',
        '/img/live-student/17.webp',

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
.slider-text {
  text-align: center;
  font-size: 14px;
  color: #333;
  margin-top: 10px;
  padding: 0 20px;
  line-height: 1.5;
}
.img-container {
  .slider {
    position: relative;
    width: 100%;
    max-width: 880px;
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

.ab__pp {
  font-size: 16px;
  font-weight: 400;
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
