<template>
  <block-ab title="Билет в будущее" class="ticket-page">
    <!-- Слайдер наград -->

    <EntitiesImgScreen :instance="visibleAwards" :images="awards" :separatePage="false" />

    <img alt="Логотип Билет в будущее" src="/img/educational/Logo-BvB.webp" class="ab__img" />

    <div class="ticket-wrapper">
      <p class="ab__p">
        Колледж является площадкой по организации и проведению практических мероприятий в очном
        формате по ранней профессиональной ориентации учащихся 8-11-х классов общеобразовательных
        организаций «Билет в будущее».
      </p>

      <p class="ab__p">
        Проект Единая модель профориентации «Билет в будущее» реализуется в рамках федерального
        проекта «Профессионалитет» национального проекта «Молодежь и дети» и направлен на
        формирование у обучающихся 6–11 классов готовности к профессиональному самоопределению.
      </p>

      <p class="ab__p">
        В ходе мероприятий школьники знакомятся с реальными условиями профессиональной деятельности,
        выполняют практические задания, работают с оборудованием, программным обеспечением и
        получают консультации от наставников — представителей соответствующих профессий.
      </p>

      <h2 class="ticket-title">Новости проекта</h2>

      <div class="ticket-news">
        <div v-for="(item, index) in filteredNews" :key="index" class="ticket-card">
          <!-- Заголовок (аккордеон) -->

          <div
            class="ticket-header"
            :class="{ active: activeNews === index }"
            @click="toggleNews(index)">
            <div class="ticket-meta">
              <span class="ticket-date">{{ item.date }}</span>

              <h3 class="ticket-name">{{ item.title }}</h3>
            </div>

            <div class="ticket-arrow">
              <svg
                width="20"
                height="20"
                viewBox="0 0 24 24"
                :class="{ rotated: activeNews === index }">
                <path
                  d="M6 9L12 15L18 9"
                  stroke="currentColor"
                  stroke-width="2"
                  fill="none"
                  stroke-linecap="round"
                  stroke-linejoin="round" />
              </svg>
            </div>
          </div>

          <!-- СЛАЙДЕР: показывается ТОЛЬКО если есть изображения -->

          <div v-if="item.images && item.images.length" class="ticket-slider">
            <button
              v-if="item.images.length > 1"
              class="slider-arrow left"
              @click.stop="prevSlide(index)">
              ‹
            </button>

            <img :src="item.images[item.currentSlide]" class="slider-img" loading="lazy" />

            <button
              v-if="item.images.length > 1"
              class="slider-arrow right"
              @click.stop="nextSlide(index)">
              ›
            </button>
          </div>

          <!-- ТЕКСТ НОВОСТИ (аккордеон) -->

          <transition name="fade">
            <div v-if="activeNews === index" class="ticket-content">
              <p v-for="(text, i) in item.content" :key="i">
                {{ text }}
              </p>
            </div>
          </transition>
        </div>
      </div>
    </div>

    <!-- TODO: Блок наставников -->

    <h2 class="ticket-title">Наставники</h2>

    <div class="mentors-grid">
      <div class="mentor-card" v-for="(mentor, index) in mentors" :key="index">
        <p class="mentor-profession">{{ mentor.profession }}</p>

        <ul class="mentor-list">
          <li v-for="(name, i) in mentor.names" :key="i">{{ name }}</li>
        </ul>
      </div>
    </div>

    <!-- TODO: СТАРОЕ -->
    <h1>Билет в будущее 2022 г.</h1>
    <p class="ab__p">
      Колледж стал площадкой для проведения практических мероприятий в рамках федерального проекта
      по ранней профессиональной ориентации учащихся 6-11-х классов общеобразовательных организаций
      «Билет в будущее» в 2022 году.
    </p>
    <p class="ab__p">
      Проект по ранней профессиональной ориентации учащихся 6-11 классов общеобразовательных
      организаций «Билет в будущее» решает задачу повышения осознанности школьников в выборе
      профессии. В рамках проекта школьники участвуют в профессиональных пробах, где имеют
      возможность на практике попробовать свои силы в интересных для себя профессиях: визуальный
      мерчандайзер, программист, повар-кондитер и предприниматель малого бизнеса.
    </p>
    <p class="ab__p">
      В рамках практических мероприятий высока роль наставника – именно он знакомит подростка с
      основной информацией о профессиональной области, под его руководством участник выполняет
      заданную рабочую операцию, получает оценку результата и обратную связь с рекомендациями по
      развитию. Выделяется три возрастных категории участников: 6-7, 8-9 и 10-11 классы.
    </p>
    <p class="ab__p">
      В ходе профессиональной пробы участники решают одну или несколько практических задач и
      выполняют реальные рабочие операции, относящиеся к конкретной профессиональной области. Проба
      подразумевает работу участников с материалами, инструментами, оборудованием, программным
      обеспечением, без игровой адаптации и в условиях, максимально приближенных к реальным.
    </p>
    <p class="ab__p">
      В ходе пробы участники взаимодействуют с наставником, являющимся носителем профессиональных
      компетенций, получая от него теоретические знания, практические рекомендации, обратную связь и
      оценку по итогам пробы.
    </p>

    <p class="ab__p">
      <b>Координатор площадки: Юрьева Елена Георгиевна</b>
      <a href="tel:8(3812) 68-07-82"> т. 8(3812) 68-07-82,</a> <b> e-mail:</b>
      <a href="mailto:tradeconomy@mail.ru">tradeconomy@mail.ru </a>
    </p>
    <h2 class="ab__subtitle">Наставники:</h2>
    <p class="ab__p">
      <b>Профессиональное направление: "Повар, кондитер" (Комфортная среда):</b>
    </p>
    <ul class="ab__list">
      <li>Федорова Галина Николаевна</li>
      <li>Подольская Тамара Васильевна</li>
      <li>Кузьменкина Наталья Александровна</li>
    </ul>
    <p class="ab__p">
      <b>Профессиональное направление: "Предприниматель малого бизнеса" (Деловая среда): </b>
    </p>
    <ul class="ab__list">
      <li>Покутная Виктория Александровна</li>
      <li>Спирина Наталья Алексеевна</li>
      <li>Аронова Светлана Владимировна</li>
    </ul>
    <p class="ab__p">
      <b>Профессиональное направление: "Товаровед-эксперт" (Деловая среда): </b>
    </p>
    <ul class="ab__list">
      <li>Ли Анна Амуровна</li>
      <li>Степанова Галина Васильевна</li>
    </ul>
    <p class="ab__p">
      <b>Профессиональное направление: "Программист" (Умная среда): </b>
    </p>
    <ul class="ab__list">
      <li>Орлова Вера Михайловна</li>
    </ul>
    <p class="ab__p">
      <b
        >Профессиональное направление: "Разработчик Web и мультимедийных приложений" (Умная среда):
      </b>
    </p>
    <ul class="ab__list">
      <li>Арнольд Юлия Алексеевна</li>
      <li>Маслова Надежда Алексеевна</li>
      <li>Смолиженко Ольга Александровна</li>
    </ul>
    <p class="ab__p">
      <b>Профессиональное направление: "Визуальный мерчандайзер" (Креативная среда): </b>
    </p>
    <ul class="ab__list">
      <li>Чукаева Людмила Ивановна</li>
    </ul>
    <p class="ab__p">
      <b>Профессиональное направление: "Официант" (Социальная среда):</b>
    </p>
    <ul class="ab__list">
      <li>Севернюк Ирина Александровна</li>
    </ul>
    <p class="ab__p">
      <b
        >Профессиональное направление: "Специалист по гостеприимству: администратор отеля"
        (Социальная среда):
      </b>
    </p>
    <ul class="ab__list">
      <li>Колиева Марина Александровна</li>
    </ul>
    <p class="ab__p">
      <b>Профессиональное направление: "Фронтенд-разработчик" (Умная среда): </b>
    </p>
    <ul class="ab__list">
      <li>Кутиков Павел Алексеевич</li>
    </ul>
    <p class="ab__p">
      <b>Профессиональное направление: "Бухгалтерский учет" (Деловая среда): </b>
    </p>
    <ul class="ab__list">
      <li>Кудинова Олеся Викторовна</li>
    </ul>
    <swiper class="slider_committe" :options="opts">
      <swiper-slide v-for="(link, imgIdx) of img" :key="imgIdx">
        <img class="img-single__minimg" alt="Slider-Image" :src="link" />
      </swiper-slide>
    </swiper>
    <common-documents-list json-path="documents/project-ticket.json" />
    <!-- <p class="ab__p"><b>Благодарности:</b></p> -->
    <swiper class="slider_committe" :options="opts">
      <swiper-slide v-for="(link, imgIdx) of awards" :key="imgIdx">
        <img
          class="img-single__minimg"
          alt="Slider-Image"
          :src="link"
          v-on:click="visibleAwards = !visibleAwards" />
      </swiper-slide>
    </swiper>
  </block-ab>
</template>

<script>
import { loadDynamic } from '~/core/helpers/file'

export default {
  data() {
    return {
      // СТАРОЕ

      news: [],
      img: [
        '/img/projects/ticket/bvb1.jpg',
        '/img/projects/ticket/bvb2.jpg',
        '/img/projects/ticket/bvb3.jpg',
        '/img/projects/ticket/bvb4.jpg',
        '/img/projects/ticket/bvb5.jpg',
        '/img/projects/ticket/bvb6.jpg',
        '/img/projects/ticket/bvb7.jpg',
        '/img/projects/ticket/bvb8.jpg',
        '/img/projects/ticket/bvb9.jpg',
        '/img/projects/ticket/bvb10.jpg',
        '/img/projects/ticket/bvb11.jpg',
        '/img/projects/ticket/bvb12.jpg',
      ],
      awards: ['/img/projects/ticket/award1.jpg'],
      visibleAwards: false,
      opts: {
        autoplay: {
          enabled: true,
          delay: 3000,
        },
      },
      // СТАРОЕ
      news: [],

      activeNews: null,

      awards: [
        '/img/projects/ticket/award1.jpg',

        '/img/projects/ticket/award2.jpg',

        '/img/projects/ticket/award3.jpg',
      ],

      visibleAwards: false,

      mentors: [
        { profession: 'Администратор гостиницы', names: ['Колиева М.А.'] },
        { profession: 'Программист 1С', names: ['Колмогорцева Ю.А.', 'Россолов Д.С.'] },
        { profession: 'Программист, фронтенд-разработчик', names: ['Кутиков П.А.'] },
        {
          profession: 'Администратор зала предприятия общественного питания',
          names: ['Севернюк И.А.'],
        },
        { profession: 'Юрисконсульт', names: ['Касенова Г.С.'] },
        { profession: 'Повар', names: ['Абилова Т.Н.'] },
        {
          profession: 'Мастер по ремонту оборудования',
          names: ['Пепеляев Е.В.', 'Ткаченко В.Н.', 'Сидоров А.Т.'],
        },
        { profession: 'Налоговый консультант', names: ['Кудинова О.В.'] },
        { profession: 'Программист', names: ['Маслова Н.А.', 'Арнольд Ю.А.', 'Смолиженко О.А.'] },
        { profession: 'Визуальный мерчендайзер', names: ['Чукаева Л.И.'] },
        { profession: 'Предприниматель', names: ['Спирина Н.А.'] },
        { profession: 'Товаровед-эксперт', names: ['Ли А.А.', 'Степанова Г.В.'] },
        { profession: 'Бухгалтер', names: ['Кудинова О.В.'] },
      ],
    }
  },

  computed: {
    filteredNews() {
      return this.news.filter((n) => n.teg === 'ticket')
    },
  },

  async created() {
    try {
      const data = JSON.parse(await loadDynamic('dynamic/news.json'))

      for (const item of data) {
        if (item.teg !== 'ticket') continue

        const dayMatch = item.date.match(/\d+/)

        const day = dayMatch ? dayMatch[0] : null

        const images = []

        if (day) {
          // Проверяем существование файлов 1.webp ... 10.webp

          for (let i = 1; i <= 10; i++) {
            const path = `/img/news/biletnewsimg/${day}/${i}.webp`

            const exists = await this.imageExists(path)

            if (exists) images.push(path)
          }
        }

        this.news.push({
          ...item,

          images,

          currentSlide: 0,
        })
      }
    } catch (e) {
      console.log('Ошибка загрузки новостей', e)
    }
  },

  methods: {
    toggleNews(index) {
      this.activeNews = this.activeNews === index ? null : index
    },

    nextSlide(index) {
      const item = this.filteredNews[index]

      if (item.images && item.images.length) {
        item.currentSlide = (item.currentSlide + 1) % item.images.length
      }
    },

    prevSlide(index) {
      const item = this.filteredNews[index]

      if (item.images && item.images.length) {
        item.currentSlide = (item.currentSlide - 1 + item.images.length) % item.images.length
      }
    },

    imageExists(path) {
      return new Promise((resolve) => {
        const img = new Image()

        img.onload = () => resolve(true)

        img.onerror = () => resolve(false)

        img.src = path
      })
    },
  },
}
</script>

<style scoped lang="scss">
.ticket-page {
  position: relative;
}

.ab__img {
  position: absolute;

  height: 200px;

  width: 200px;

  right: 24px;

  top: 24px;

  z-index: 1;

  @include high-medium-media() {
    width: 150px;

    height: 150px;

    right: 12px;

    top: 10px;

    opacity: 0.4;
  }
}

.ticket-wrapper {
  max-width: 1000px;

  @media (max-width: 768px) {
    padding: 0 0 40px;
  }
}

.ticket-title {
  font-size: 28px;

  margin-top: 2.5rem;

  margin-bottom: 1.5rem;

  font-weight: 700;

  position: relative;

  display: inline-block;

  &::after {
    content: '';

    position: absolute;

    bottom: -8px;

    left: 0;

    width: 60px;

    height: 3px;

    background: linear-gradient(90deg, #c43e3e, #e67e7e);

    border-radius: 2px;
  }
}

h1 {
  font-size: 30px;
  font-weight: bold;
  color: #c43e3e;
  padding-top: 20px;
  padding-bottom: 5px;
}

.ticket-news {
  display: flex;

  flex-direction: column;

  gap: 28px;
}

.ticket-card {
  background: white;

  border-radius: 16px;

  padding: 26px;

  box-shadow: 0 6px 20px rgba(0, 0, 0, 0.05);

  border: 1px solid #f0f0f0;

  transition: 0.3s ease;

  &:hover {
    box-shadow: 0 12px 28px rgba(0, 0, 0, 0.1);
  }
}

.ticket-header {
  display: flex;

  justify-content: space-between;

  align-items: center;

  cursor: pointer;

  gap: 20px;
}

.ticket-meta {
  flex: 1;
}

.ticket-date {
  background: #c43e3e;

  color: white;

  padding: 5px 14px;

  border-radius: 30px;

  font-size: 12px;

  font-weight: 600;

  display: inline-block;
}

.ticket-name {
  margin-top: 10px;

  font-size: 19px;

  font-weight: 600;

  color: #1a2634;
}

.ticket-arrow svg {
  transition: transform 0.3s ease;

  stroke: currentColor;
}

.ticket-arrow svg.rotated {
  transform: rotate(180deg);
}

.ticket-slider {
  margin-top: 20px;

  position: relative;

  border-radius: 14px;

  overflow: hidden;
}

.slider-img {
  width: 100%;

  object-fit: cover;

  display: block;

  background: #f5f5f5;

  @media (max-width: 768px) {
    height: 220px;
  }
}

.slider-arrow {
  position: absolute;

  top: 50%;

  transform: translateY(-50%);

  background: rgba(0, 0, 0, 0.5);

  color: white;

  border: none;

  width: 40px;

  height: 40px;

  border-radius: 50%;

  cursor: pointer;

  font-size: 22px;

  display: flex;

  align-items: center;

  justify-content: center;

  transition: background 0.2s;

  z-index: 2;

  &:hover {
    background: #c43e3e;
  }

  &.left {
    left: 10px;
  }

  &.right {
    right: 10px;
  }

  @media (max-width: 768px) {
    width: 32px;

    height: 32px;

    font-size: 18px;
  }
}

.ticket-content {
  margin-top: 22px;

  padding-top: 18px;

  border-top: 1px dashed #eee;

  p {
    margin-bottom: 14px;

    line-height: 1.6;

    color: #2c3e50;

    font-size: 0.95rem;

    &:last-child {
      margin-bottom: 0;
    }
  }
}

.fade-enter-active,
.fade-leave-active {
  transition: all 0.3s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;

  transform: translateY(-8px);
}

// TODO: СТИЛИ НАСТАВНИКОВ

.mentors-grid {
  display: grid;

  grid-template-columns: repeat(2, 1fr);

  gap: 20px;

  margin-top: 1.5rem;

  @media (max-width: 768px) {
    grid-template-columns: 1fr;

    gap: 16px;
  }
}

.mentor-card {
  background: #fafafa;

  border-radius: 12px;

  padding: 18px 20px;

  border: 1px solid #f0f0f0;

  transition: box-shadow 0.2s;

  &:hover {
    box-shadow: 0 6px 16px rgba(0, 0, 0, 0.04);
  }
}

.mentor-profession {
  font-weight: 700;

  font-size: 1.1rem;

  color: #1a2634;

  margin: 0 0 10px 0;

  position: relative;

  padding-bottom: 6px;

  border-bottom: 2px solid #c43e3e20;

  &::after {
    content: '';

    position: absolute;

    bottom: -2px;

    left: 0;

    width: 40px;

    height: 2px;

    background: #c43e3e;

    border-radius: 2px;
  }
}

.mentor-list {
  list-style: none;

  padding: 0;

  margin: 0;

  li {
    padding: 6px 0;

    font-size: 0.95rem;

    color: #2c3e50;

    border-bottom: 1px dashed #eee;

    &:last-child {
      border-bottom: none;
    }
  }
}
</style>
