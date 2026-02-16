<template>
  <block-ab title="Билет в будущее">
    <!-- Слайдер наград -->
    <EntitiesImgScreen :instance="visibleAwards" :images="awards" :separatePage="false" />

    <img alt="Логотип Билет в будущее" src="/img/educational/Logo-BvB.webp" class="ab__img" />

    <p class="ab__p">
      Колледж является площадкой по организации и проведению практических мероприятий в очном
      формате по ранней профессиональной ориентации учащихся 8-11-х классов общеобразовательных
      организаций «Билет в будущее».
    </p>

    <p class="ab__p">
      Проект Единая модель профориентации «Билет в будущее» реализуется в рамках федерального
      проекта «Профессионалитет» национального проекта «Молодежь и дети» и направлен на формирование
      у обучающихся 6–11 классов готовности к профессиональному самоопределению.
    </p>

    <p class="ab__p">
      В ходе мероприятий школьники знакомятся с реальными условиями профессиональной деятельности,
      выполняют практические задания, работают с оборудованием, программным обеспечением и получают
      консультации от наставников — представителей соответствующих профессий.
    </p>

    <!-- Новости проекта: сетка 2 колонки на ПК, 1 на телефоне -->
    <h2 class="ab__subtitle ab__news-title">Новости проекта</h2>

    <div class="news-grid">
      <div
        v-for="(item, index) in news.filter((n) => n.teg === 'ticket')"
        :key="index"
        class="news-card">
        <!-- Верхняя часть новости (кликабельная) -->
        <div class="news-header" @click="toggleNews(index)">
          <div class="news-meta">
            <span class="news-date">{{ item.date }}</span>
            <h3 class="news-title">{{ item.title }}</h3>
          </div>

          <button class="news-toggle-btn" :class="{ active: activeNews === index }">
            <span class="toggle-text">{{ activeNews === index ? 'Скрыть' : 'Подробнее' }}</span>
            <svg
              class="toggle-icon"
              :class="{ rotated: activeNews === index }"
              width="16"
              height="16"
              viewBox="0 0 24 24"
              fill="none"
              xmlns="http://www.w3.org/2000/svg">
              <path
                d="M7 10L12 15L17 10"
                stroke="currentColor"
                stroke-width="2"
                stroke-linecap="round"
                stroke-linejoin="round" />
            </svg>
          </button>
        </div>

        <!-- Фото новости (уменьшенное, всегда видно) -->
        <img
          v-if="item.image"
          :src="item.image"
          class="news-image"
          alt="Фото новости"
          loading="lazy" />

        <!-- Полный текст с анимацией -->
        <transition name="fade">
          <div v-if="activeNews === index" class="news-content">
            <p v-for="(text, i) in item.content" :key="i" class="ab__p">
              {{ text }}
            </p>
          </div>
        </transition>
      </div>
    </div>
  </block-ab>
</template>

<script>
import { loadDynamic } from '~/core/helpers/file'

export default {
  data() {
    return {
      news: [],
      activeNews: null,
      awards: ['/img/projects/ticket/award1.jpg'],
      visibleAwards: false,
    }
  },
  async created() {
    try {
      this.news = JSON.parse(await loadDynamic('dynamic/news.json'))
    } catch (e) {
      console.log('Проверьте валидность JSON новостей и событий!', e)
    }
  },
  methods: {
    toggleNews(index) {
      this.activeNews = this.activeNews === index ? null : index
    },
  },
}
</script>

<style scoped lang="scss">
// Логотип в углу
.ab__img {
  position: absolute;
  height: 200px;
  width: 200px;
  right: 24px;
  top: 24px;

  @include high-medium-media() {
    width: 150px;
    height: 150px;
    right: 12px;
    top: 10px;
    opacity: 0.4;
  }
}

// Заголовок раздела новостей
.ab__news-title {
  margin-top: 2.5rem;
  margin-bottom: 1.5rem;
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

// Сетка новостей: 2 колонки на десктопе, 1 на планшете/телефоне
.news-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 24px;

  @media (max-width: 768px) {
    grid-template-columns: 1fr;
    gap: 20px;
  }
}

// Карточка новости
.news-card {
  display: flex;
  flex-direction: column;
  border-radius: 16px;
  padding: 20px;
  background: #ffffff;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.04);
  transition: box-shadow 0.3s ease, transform 0.2s ease;
  border: 1px solid #f0f0f0;
  height: fit-content;

  &:hover {
    box-shadow: 0 12px 24px rgba(0, 0, 0, 0.08);
    transform: translateY(-2px);
  }
}

// Шапка новости (кликабельная область)
.news-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  cursor: pointer;
  gap: 16px;

  @media (max-width: 768px) {
    flex-direction: column;
    align-items: flex-start;
    gap: 12px;
  }
}

// Блок с датой и заголовком
.news-meta {
  flex: 1;
}

.news-date {
  display: inline-block;
  font-size: 0.75rem;
  font-weight: 600;
  color: #ffffff;
  background: #c43e3e;
  padding: 4px 12px;
  border-radius: 30px;
  letter-spacing: 0.3px;
  text-transform: uppercase;
  margin-bottom: 8px;
}

.news-title {
  font-size: 1.1rem;
  margin: 0;
  color: #1a2634;
  font-weight: 600;
  line-height: 1.4;

  @media (max-width: 768px) {
    font-size: 1rem;
  }
}

// Кнопка переключения (компактная)
.news-toggle-btn {
  display: flex;
  align-items: center;
  gap: 6px;
  background: none;
  border: 1px solid #e0e0e0;
  border-radius: 40px;
  padding: 6px 14px;
  font-size: 0.85rem;
  font-weight: 500;
  color: #555;
  transition: all 0.2s ease;
  cursor: pointer;
  white-space: nowrap;

  &:hover {
    background: #f9f9f9;
    border-color: #c43e3e;
    color: #c43e3e;
  }

  &.active {
    background: #c43e3e;
    border-color: #c43e3e;
    color: white;

    &:hover {
      background: #b03030;
    }
  }

  @media (max-width: 768px) {
    width: 100%;
    justify-content: center;
    padding: 8px 16px;
  }
}

.toggle-text {
  line-height: 1;
}

.toggle-icon {
  transition: transform 0.3s ease;
  stroke-width: 2.2;

  &.rotated {
    transform: rotate(180deg);
  }
}

// Изображение новости — уменьшенное, аккуратное
.news-image {
  width: 100%;
  height: 180px; /* фиксированная высота для единообразия */
  object-fit: cover;
  border-radius: 12px;
  margin-top: 16px;
  box-shadow: 0 6px 14px rgba(0, 0, 0, 0.06);
  transition: transform 0.3s ease;

  &:hover {
    transform: scale(1.01);
  }

  @media (max-width: 768px) {
    height: 160px; /* чуть меньше на телефоне */
  }
}

// Полный текст новости
.news-content {
  margin-top: 20px;
  padding-top: 16px;
  border-top: 1px dashed #eaeaea;

  .ab__p {
    margin-bottom: 0.9rem;
    font-size: 0.95rem;
    line-height: 1.6;
    color: #2c3e50;
  }
}

// Анимация появления / исчезновения
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.4s ease, transform 0.4s cubic-bezier(0.25, 0.8, 0.25, 1);
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
  transform: translateY(-10px);
}

// Дополнительная адаптация для маленьких экранов
@media (max-width: 480px) {
  .news-card {
    padding: 16px;
  }

  .news-title {
    font-size: 0.95rem;
  }

  .news-image {
    height: 140px;
  }

  .news-content .ab__p {
    font-size: 0.9rem;
  }
}
</style>
