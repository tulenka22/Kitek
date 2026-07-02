<template>
  <div class="projects-page">
    <header class="page-header">
      <div class="header-top">
        <div class="header-copy">
          <p class="eyebrow">КИТЭК</p>
          <h1 class="main-title" style="color: #c43e3e;">Студенческие проекты</h1>
        </div>
      </div>
    </header>

    <section class="projects-section">
      <div class="projects-container">
        <article
          class="project-card"
          ref="card1"
          :class="{ revealed: card1Visible }"
        >
          <div class="card-inner">
            <div class="card-number">01</div>
            <h2 class="project-title">Река. Слово. След</h2>
            <p class="project-desc">
              Проект «Река. Слово. След» направлен на изучение уникальной культуры, исторического наследия и природы Западной Сибири, включая традиции, архитектурные памятники и природные объекты. Его цель заключается в распространении краеведческих знаний об Обь-Иртышском бассейне. Практическая значимость проекта заключается в сохранении локального культурно-исторического наследия, воспитании патриотизма и гражданской идентичности, трансляции традиций и ценностей многонационального российского государства, в формировании у жителей и гостей региона глубокого понимания и уважения к местным традициям и истории, развитии туризма и культурного обмена.
            </p>
            <a href="/data/site-project/Паспорт-проекта_Завалий-Н.Ф._-Наумова-А.А._-Шертман-И.Р.-Река.-Слово.-След-_3_ (1).pdf" class="project-link" >
              Паспорт проекта
            </a>
            <a href="/student/student-site" class="project-link">
            Начать путешествие
            </a>
          </div>
        </article>

        <article
          class="project-card"
          ref="card2"
          :class="{ revealed: card2Visible }"
        >
          <div class="card-inner">
            <div class="card-number">02</div>
            <h2 class="project-title">Легенды и божества речных берегов: мифологическая карта Обь-Иртышского бассейна</h2>
            <p class="project-desc">
              Проект посвящён созданию интерактивного экскурсионного маршрута по сакральным местам Обь-Иртышского бассейна, связанного с мифологическими сюжетами, легендами и традиционными верованиями коренных народов Сибири. В его основе - мифологическая карта Обь-Иртышского бассейна с точками маршрута, снабженная текстовыми материалами, аудиозаписями легенд, фотографиями, иллюстрациями, короткими аудио-подкастами, промо-роликами, которые помогают познакомиться с культурным наследием региона и повысить доступность, наглядность и привлекательность сложного этнографического материала.
            </p>
            <a href="/data/site-project/Паспорт-проекта-Разработка-экскурсионного-маршрута-_1_.pdf" class="project-link" >
              Паспорт проекта
            </a>
            <a href="https://clck.ru/3Tbv55" class="project-link">
                Начать экскурсию
            </a>
          </div>
        </article>

        <article
          class="project-card"
          ref="card3"
          :class="{ revealed: card3Visible }"
        >
          <div class="card-inner">
            <div class="card-number">03</div>
            <h2 class="project-title">Экспертиза качества и оптимизация профессиональной химии для снижения экологического следа</h2>
            <p class="project-desc">
              Проект посвящен анализу профессиональной химии с точки зрения ее качества, безопасности и влияния на окружающую среду. В ходе работы изучается состав, экологический след и возможность замены профессиональных средств, применяемых на предприятиях торговли, туризма и гостеприимства, на более безопасные и эффективные решения в рамках принципов «зеленой химии»
            </p>
            <a href="/data/site-project/Паспорт-проекта_Ли-А.А.-_1_.pdf" class="project-link" >
              Паспорт проекта
            </a>
          </div>
        </article>
      </div>
    </section>
  </div>
</template>

<script>
export default {
  name: 'StudentProjects',

  data() {
    return {
      card1Visible: false,
      card2Visible: false,
      card3Visible: false
    }
  },

  mounted() {
    window.addEventListener('scroll', this.handleScroll, { passive: true })
    this.handleScroll()
  },

  beforeDestroy() {
    window.removeEventListener('scroll', this.handleScroll)
  },

  methods: {
    handleScroll() {
      const cards = [
        { ref: 'card1', prop: 'card1Visible' },
        { ref: 'card2', prop: 'card2Visible' },
        { ref: 'card3', prop: 'card3Visible' }
      ]

      cards.forEach(({ ref, prop }) => {
        const card = this.$refs[ref]
        if (!card) return
        const rect = card.getBoundingClientRect()
        if (rect.top < window.innerHeight * 0.9) {
          this[prop] = true
        }
      })
    },

    navigateTo(route) {
      console.log('Navigate to:', route)
    }
  }
}
</script>

<style scoped>
.projects-page {
  min-height: 100vh;
  background: #f5f5f2;
  color: #111;
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
  overflow-x: hidden;
}

.page-header {
  padding: 2rem 1.5rem 0;
}

.header-top {
  max-width: 1200px;
  margin: 0 auto;
}

.header-copy {
  max-width: 720px;
}

/* Акцентный цвет #c43e3e для надзаголовка */
.eyebrow {
  margin: 0 0 0.75rem;
  font-size: 0.85rem;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: #c43e3e;
}

.main-title {
  margin: 0;
  font-size: clamp(2rem, 5vw, 4.5rem);
  line-height: 1.05;
  font-weight: 800;
  color: #111;
}

.projects-section {
  padding: 3rem 1.5rem 6rem;
}

.projects-container {
  max-width: 1200px;
  margin: 0 auto;
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 1.5rem;
}

.project-card {
  position: relative;
  border-radius: 22px;
  background: #fff;
  border: 1px solid #d9d9d9;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.04);
  opacity: 0;
  transform: translateY(30px);
  transition: transform 0.35s ease, box-shadow 0.35s ease, border-color 0.35s ease;
  overflow: hidden;
}

.project-card.revealed {
  opacity: 1;
  transform: translateY(0);
}

.project-card:hover {
  transform: translateY(-6px);
  border-color: #c43e3e;
  box-shadow: 0 16px 40px rgba(196, 62, 62, 0.12);
}

.card-inner {
  padding: 2rem;
  display: flex;
  flex-direction: column;
  gap: 1rem;
  min-height: 320px;
}

/* Номер проекта #c43e3e с прозрачностью */
.card-number {
  font-size: 3.5rem;
  line-height: 1;
  font-weight: 900;
  color: rgba(196, 62, 62, 0.12);
}

.project-title {
  margin: 0;
  font-size: 1.45rem;
  line-height: 1.2;
  font-weight: 700;
  color: #111;
}

.project-desc {
  margin: 0;
  font-size: 0.98rem;
  line-height: 1.7;
  color: #555;
  flex: 1;
}

/* Кнопка-ссылка в цвете #c43e3e */
.project-link {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: fit-content;
  padding: 0.9rem 1.2rem;
  border-radius: 12px;
  background: #c43e3e;
  color: #fff;
  text-decoration: none;
  font-weight: 600;
  border: 1px solid #c43e3e;
  transition: all 0.25s ease;
}

.project-link:hover {
  background: #fff;
  color: #c43e3e;
  transform: translateY(-1px);
}

@media (max-width: 1024px) {
  .projects-container {
    grid-template-columns: 1fr;
  }
}

@media (max-width: 768px) {
  .page-header {
    padding-top: 1.25rem;
  }

  .projects-section {
    padding: 2rem 1rem 4rem;
  }

  .card-inner {
    min-height: auto;
    padding: 1.5rem;
  }

  .project-title {
    font-size: 1.25rem;
  }
}
</style>
