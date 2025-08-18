<template>
  <div class="admission-container">
    <!-- Баннер (только изображение) -->
    <div class="top-banner">
      <img
        src="https://images.unsplash.com/photo-1504384308090-c894fdcc538d?auto=format&fit=crop&w=1600&q=80"
        alt="Учебный процесс"
        class="banner-image" />
    </div>

    <!-- Таблица специальностей -->
    <div class="professions-table" ref="professionsSection">
      <h2 class="section-title">Специальности нашего колледжа</h2>
      <p class="section-subtitle">Выберите интересующую специальность для подробной информации</p>

      <div class="table-header">
        <div class="icon-col"></div>
        <div class="name-col">Специальности</div>
        <div class="full-time-col">Очное</div>
        <div class="part-time-col">Заочное</div>
      </div>

      <div class="profession-item" v-for="(prof, index) in professions" :key="prof.code">
        <div
          class="table-row"
          @click="toggleProfession(index)"
          :class="{ active: openProfessions.includes(index) }"
          tabindex="0"
          @keydown.enter.space.prevent="toggleProfession(index)">
          <div class="icon-col">
            <div class="profession-icon">
              <!-- Здесь будет ваша картинка -->
              <img :src="prof.image" :alt="prof.name" class="icon-image" />
            </div>
          </div>
          <div class="name-col">
            <div class="code">{{ prof.code }}</div>
            <div class="name">{{ prof.name }}</div>
            <div class="specialization" v-if="prof.specialization">{{ prof.specialization }}</div>
          </div>
          <div class="full-time-col">
            <div class="study-type">Очное</div>
            <div class="grades">
              <div class="grade-9">
                <span class="label">9 кл:</span>
                <span class="budget" v-if="prof.fullTime.grade9.budget">{{
                  prof.fullTime.grade9.budget
                }}</span>
                <span class="paid" v-if="prof.fullTime.grade9.paid">{{
                  prof.fullTime.grade9.paid
                }}</span>
                <span v-if="!prof.fullTime.grade9.budget && !prof.fullTime.grade9.paid">-</span>
              </div>
              <div class="grade-11">
                <span class="label">11 кл:</span>
                <span class="budget" v-if="prof.fullTime.grade11.budget">{{
                  prof.fullTime.grade11.budget
                }}</span>
                <span class="paid" v-if="prof.fullTime.grade11.paid">{{
                  prof.fullTime.grade11.paid
                }}</span>
                <span v-if="!prof.fullTime.grade11.budget && !prof.fullTime.grade11.paid">-</span>
              </div>
            </div>
          </div>
          <div class="part-time-col">
            <div class="study-type">Заочное</div>
            <div class="grades">
              <div class="grade-9">
                <span class="label">9 кл:</span>
                <span class="paid" v-if="prof.partTime.grade9.paid">{{
                  prof.partTime.grade9.paid
                }}</span>
                <span v-else>-</span>
              </div>
              <div class="grade-11">
                <span class="label">11 кл:</span>
                <span class="budget" v-if="prof.partTime.grade11.budget">{{
                  prof.partTime.grade11.budget
                }}</span>
                <span v-else>-</span>
              </div>
            </div>
          </div>
        </div>

        <!-- Описание специальности -->
        <transition name="slide">
          <div v-if="openProfessions.includes(index)" class="profession-description">
            <h3>
              {{ prof.name }}
              <span v-if="prof.specialization">({{ prof.specialization }})</span>
            </h3>
            <div class="total-places">
              Всего мест: <strong>{{ prof.total }}</strong>
            </div>
            <p>{{ prof.description }}</p>
            <div class="advantages" v-if="prof.advantages && prof.advantages.length">
              <div class="advantage" v-for="(adv, i) in prof.advantages" :key="i">
                <svg width="24" height="24" viewBox="0 0 24 24" class="advantage-icon">
                  <path
                    d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41L9 16.17z"
                    fill="#27ae60" />
                </svg>
                <span>{{ adv }}</span>
              </div>
            </div>
          </div>
        </transition>
      </div>
    </div>

    <!-- Шаги поступления -->
    <div class="admission-steps">
      <h2 class="section-title">Как поступить в наш колледж</h2>
      <p class="section-subtitle">Пошаговая инструкция для абитуриентов</p>

      <div class="steps-container">
        <div class="step" v-for="(step, index) in steps" :key="index">
          <div
            class="step-header"
            @click="toggleStep(index)"
            tabindex="0"
            @keydown.enter.space.prevent="toggleStep(index)">
            <div class="step-number">{{ index + 1 }}</div>
            <h3>{{ step.title }}</h3>
            <span class="arrow" :class="{ open: openSteps.includes(index) }">
              <svg width="24" height="24" viewBox="0 0 24 24">
                <path
                  d="M7.41 8.59L12 13.17l4.59-4.58L18 10l-6 6-6-6 1.41-1.41z"
                  fill="currentColor" />
              </svg>
            </span>
          </div>
          <transition name="fade">
            <div v-if="openSteps.includes(index)" class="step-content">
              <p>{{ step.description }}</p>
              <ul v-if="step.details">
                <li v-for="(detail, i) in step.details" :key="i">
                  <svg width="16" height="16" viewBox="0 0 24 24" class="list-icon">
                    <path
                      d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm0 18c-4.41 0-8-3.59-8-8s3.59-8 8-8 8 3.59 8 8-3.59 8-8 8z"
                      fill="#3498db" />
                  </svg>
                  {{ detail }}
                </li>
              </ul>
              <div class="step-notes" v-if="step.notes">
                <svg width="20" height="20" viewBox="0 0 24 24" class="note-icon">
                  <path
                    d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm1 15h-2v-2h2v2zm0-4h-2V7h2v6z"
                    fill="#f39c12" />
                </svg>
                <p>{{ step.notes }}</p>
              </div>
            </div>
          </transition>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      openProfessions: [],
      openSteps: [],
      professions: [
        {
          code: '09.02.07',
          name: 'Информационные системы и программирование',
          image: '/img/spec/isp1.jpg',
          fullTime: { grade9: { budget: 75, paid: 25 }, grade11: { budget: 0, paid: 0 } },
          partTime: { grade9: { paid: 0 }, grade11: { budget: 0 } },
          total: 100,
          description:
            'Специальность, связанная с разработкой и поддержкой информационных систем и программного обеспечения. Подходит для тех, кто любит технологии и программирование. Вы научитесь создавать современные веб-приложения, работать с базами данных и разрабатывать программное обеспечение.',
          advantages: [
            'Высокий спрос на рынке труда',
            'Возможность работать в IT-компаниях',
            'Современные методы обучения',
            'Практико-ориентированный подход',
            'Стажировки в ведущих компаниях',
          ],
        },
        {
          code: '38.02.08',
          name: 'Торговое дело',
          specialization: 'Коммерция',
          image: '/img/spec/tovarced1.jpg',
          fullTime: { grade9: { budget: 50, paid: 0 }, grade11: { budget: 25, paid: 0 } },
          partTime: { grade9: { paid: 0 }, grade11: { budget: 0 } },
          total: 95,
          description:
            'Специальность, направленная на обучение навыкам торговли, коммерции и ведения бизнеса. Отличный выбор для коммуникабельных и целеустремленных. Программа включает изучение основ маркетинга, менеджмента, логистики и финансов.',
          advantages: [
            'Практические навыки ведения бизнеса',
            'Возможность стажировок в компаниях',
            'Широкие карьерные перспективы',
            'Обучение у практикующих специалистов',
            'Развитие предпринимательских навыков',
          ],
        },
        {
          code: '38.02.08',
          name: 'Торговое дело',
          specialization: 'Товароведение',
          image: '/img/spec/tovarced2.jpg',
          fullTime: { grade9: { budget: 50, paid: 0 }, grade11: { budget: 25, paid: 0 } },
          partTime: { grade9: { paid: 0 }, grade11: { budget: 0 } },
          total: 75,
          description:
            'Специальность, направленная на изучение товарного ассортимента, контроля качества и организации товарооборота. Подходит для тех, кто интересуется логистикой и управлением запасами.',
          advantages: [
            'Знания в области товароведения',
            'Практические навыки работы с ассортиментом',
            'Возможность трудоустройства в торговых компаниях',
            'Обучение у опытных специалистов',
            'Перспективы карьерного роста',
          ],
        },
        {
          code: '38.02.01',
          name: 'Экономика и бухгалтерский учет (по отраслям)',
          image: '/img/spec/tovarced2.jpg',
          fullTime: { grade9: { budget: 50, paid: 0 }, grade11: { budget: 25, paid: 0 } },
          partTime: { grade9: { paid: 0 }, grade11: { budget: 0 } },
          total: 75,
          description:
            'Специальность для тех, кто хочет изучать экономику, бухгалтерский учет и финансовый анализ в различных отраслях. Обучение включает современные методы учета и налогообложения.',
          advantages: [
            'Актуальные знания по бухгалтерии и экономике',
            'Практические занятия и кейсы',
            'Возможность работы в бухгалтерских и финансовых отделах',
            'Подготовка к профессиональным экзаменам',
            'Стажировки и практика на предприятиях',
          ],
        },
        {
          code: '40.02.04',
          name: 'Юриспруденция',
          image: '/img/spec/komerc2.jpg',
          fullTime: { grade9: { budget: 0, paid: 25 }, grade11: { budget: 0, paid: 0 } },
          partTime: { grade9: { paid: 20 }, grade11: { budget: 0 } },
          total: 45,
          description:
            'Специальность для тех, кто хочет изучать основы права, законодательство и правоприменительную практику. Подходит для будущих юристов и специалистов правовой сферы.',
          advantages: [
            'Глубокие знания законодательства',
            'Практические занятия и судебные кейсы',
            'Возможность прохождения стажировок в юридических компаниях',
            'Подготовка к государственной аттестации',
            'Перспективы трудоустройства в государственных и частных структурах',
          ],
        },
        {
          code: '43.02.16',
          name: 'Туризм и гостеприимство',
          specialization: 'Гостиничные услуги',
          image: '/img/spec/gostinDelo2.jpg',
          fullTime: { grade9: { budget: 25, paid: 0 }, grade11: { budget: 0, paid: 0 } },
          partTime: { grade9: { paid: 0 }, grade11: { budget: 0 } },
          total: 25,
          description:
            'Специальность для тех, кто хочет работать в гостиничном бизнесе, обеспечивать комфорт и сервис для гостей. Обучение включает управление гостиницами и сервисное обслуживание.',
          advantages: [
            'Практические навыки работы в гостиницах',
            'Возможность прохождения практики в отелях',
            'Знания современных стандартов сервиса',
            'Перспективы карьерного роста в индустрии туризма',
            'Обучение у профессионалов отрасли',
          ],
        },
        {
          code: '43.02.16',
          name: 'Туризм и гостеприимство',
          specialization: 'Экскурсионные услуги',
          image: '/img/spec/buhgalter1.jpg',
          fullTime: { grade9: { budget: 25, paid: 0 }, grade11: { budget: 0, paid: 0 } },
          partTime: { grade9: { paid: 0 }, grade11: { budget: 0 } },
          total: 25,
          description:
            'Специальность для тех, кто хочет работать экскурсоводом или организатором туристических маршрутов. Обучение включает историю, культуру и основы туризма.',
          advantages: [
            'Знания по организации экскурсий',
            'Практика с реальными туристическими группами',
            'Развитие коммуникативных навыков',
            'Возможность работы в туристических агентствах',
            'Обучение у опытных экскурсоводов',
          ],
        },
        {
          code: '43.01.09',
          name: 'Повар, кондитер',
          image: '/img/spec/povar2.jpg',
          fullTime: { grade9: { budget: 100, paid: 0 }, grade11: { budget: 0, paid: 0 } },
          partTime: { grade9: { paid: 0 }, grade11: { budget: 0 } },
          total: 100,
          description:
            'Специальность для творческих и трудолюбивых людей, желающих овладеть искусством кулинарии и кондитерского мастерства. Программа включает практические занятия в современных кулинарных лабораториях под руководством опытных шеф-поваров.',
          advantages: [
            'Практические занятия на современной базе',
            'Возможность участия в конкурсах и выставках',
            'Перспективы работы в ресторанах и кафе',
            'Обучение у мастеров кулинарного искусства',
            'Современное оборудование и технологии',
          ],
        },
        {
          code: '43.02.15',
          name: 'Поварское и кондитерское дело',
          image: '/img/spec/povar3.jpg',
          fullTime: { grade9: { budget: 100, paid: 0 }, grade11: { budget: 25, paid: 0 } },
          partTime: { grade9: { paid: 0 }, grade11: { budget: 0 } },
          total: 125,
          description:
            'Специальность для творческих и трудолюбивых людей, желающих овладеть искусством кулинарии и кондитерского мастерства. Программа включает практические занятия в современных кулинарных лабораториях под руководством опытных шеф-поваров.',
          advantages: [
            'Практические занятия на современной базе',
            'Возможность участия в конкурсах и выставках',
            'Перспективы работы в ресторанах и кафе',
            'Обучение у мастеров кулинарного искусства',
            'Современное оборудование и технологии',
          ],
        },
        {
          code: '26.01.09',
          name: 'Моторист судовой',
          image: '/img/spec/esu2.jpg',
          fullTime: { grade9: { budget: 25, paid: 0 }, grade11: { budget: 0, paid: 0 } },
          partTime: { grade9: { paid: 0 }, grade11: { budget: 0 } },
          total: 25,
          description:
            'Специалист по обслуживанию и ремонту судовых двигателей и механизмов. Включает изучение технических основ и практические навыки работы с судовым оборудованием.',
          advantages: [
            'Практические навыки технического обслуживания',
            'Возможность работы на судах и в портах',
            'Обучение современным технологиям',
            'Перспективы карьерного роста',
            'Стажировки на предприятиях морского транспорта',
          ],
        },
        {
          code: '26.02.05',
          name: 'Эксплуатация судовых энергетических установок',
          image: '/img/spec/esu1.jpg',
          fullTime: { grade9: { budget: 50, paid: 0 }, grade11: { budget: 0, paid: 0 } },
          partTime: { grade9: { paid: 0 }, grade11: { budget: 0 } },
          total: 50,
          description:
            'Специалист по эксплуатации и ремонту энергетических установок судов. Обучение включает теорию и практику работы с двигателями и энергетическими системами.',
          advantages: [
            'Глубокие технические знания',
            'Практические занятия на современном оборудовании',
            'Возможность работы на судах и предприятиях морского транспорта',
            'Подготовка к профессиональной деятельности',
            'Стажировки и практика на профильных предприятиях',
          ],
        },
      ],

      steps: [
        {
          title: 'Поступление после 9 класса / Поступление после 11 класса',
          description: 'Основные этапы получения аттестата для поступления.',
          details: [
            'Поступление после 9 класса: Сдайте ОГЭ и получите аттестат об основном общем образовании',
            'Поступление после 11 класса: Сдайте ЕГЭ и получите аттестат о среднем общем образовании',
          ],
          notes: '',
        },
        {
          title: 'Выбор специальности',
          description: 'Выберите специальность и программу колледжа.',
          details: [
            'Определитесь с направлением подготовки, которое соответствует вашим интересам и способностям.',
            'Посетите день открытых дверей колледжа',
            'Пообщайтесь с преподавателями и студентами',
            'Изучите перспективы трудоустройства после обучения',
            'Ознакомьтесь с учебными планами',
            'Выберите специальность и программу колледжа на https://omsktec.ru/specialties',
          ],
          notes:
            'Вы можете подать документы на несколько специальностей одновременно (до 3 направлений).',
        },
        {
          title: 'Подготовка документов',
          description: 'Соберите необходимый пакет документов для подачи в приемную комиссию.',

          details: [
            'Для граждан РФ:',
            '  - оригинал или копия документа, удостоверяющего личность',
            '  - СНИЛС (копия)',
            '  - оригинал или копия документа об образовании',
            '  - 4 фотографии 3×4 см (цветные, матовые)',
            'Для иностранных граждан или лиц без гражданства:',
            '  - копия документа, удостоверяющего личность, либо документ, удостоверяющий личность иностранного гражданина',
            '  - оригинал документа государственного образца об образовании (или заверенная копия)',
            '  - заверенный перевод на русский язык документа иностранного государства об уровне образования и (или) квалификации и приложение к нему',
            '  - копии документов или иных доказательств, подтверждающих принадлежность к группам, предусмотренным статьей 17 Федерального закона № 99-ФЗ',
            '  - 4 фотографии 3×4 см',
            'Дополнительно:',
            '  - Медицинская справка 086/у (действительна 6 месяцев)',
            '  - Паспорт (копия + оригинал для сверки)',
            '  - Для льготных категорий - документы, подтверждающие льготу',
            '  - Для иногородних студентов - копия регистрации по месту жительства',
          ],
          notes: 'Проверьте полный список документов в приемной комиссии.',
        },
        {
          title: 'Подача заявления',
          description: 'Подайте документы в приемную комиссию в установленные сроки.',
          details: [
            'Со 2 июня до 15 августа (включительно) подайте личное заявление и пакет документов на очную форму образования в Приемную комиссию «КИТЭК»',
            'Со 2 июня до 1 декабря (включительно) подайте личное заявление и пакет документов на заочную форму образования',
            'Адрес: г. Омск, ул. 27-я Северная, 69',
            'Телефон: 8 (3812) 68-07-66',
            'Варианты подачи документов:',
            '  - Лично в приемной комиссии колледжа (пн-пт с 9:00 до 17:00)',
            '  - Через портал Госуслуг (для некоторых специальностей)',
            '  - Через операторов почтовой связи (заказным письмом с уведомлением)',
          ],
          notes:
            'Рекомендуется подавать документы в первые дни приемной кампании для увеличения шансов на зачисление.',
        },
        {
          title: 'Вступительные испытания',
          description: 'Пройти конкурсный отбор или вступительные испытания (если требуются).',
          details: [
            'Для творческих специальностей - практический экзамен (даты уточняйте)',
            'Для некоторых направлений - собеседование с приемной комиссией',
            'Конкурс аттестатов для выпускников 9 и 11 классов (средний балл)',
          ],
          notes:
            'Результаты ЕГЭ не требуются для поступления в колледж, учитывается средний балл аттестата.',
        },
        {
          title: 'Зачисление',
          description: 'Дождитесь приказа о зачислении и завершите оформление.',
          details: [
            'Оригинал документа об образовании должен быть предоставлен до зачисления',
            'Ознакомьтесь с приказом о зачислении на сайте колледжа',
            'Посетите организационное собрание для первокурсников',
            'Заключите договор на обучение (для платных мест)',
            'Получите студенческий билет и зачетную книжку',
            'После зачисления необходимо в течение 5 рабочих дней оформить все документы для начала обучения',
          ],
          notes: '',
        },
      ],
    }
  },
  methods: {
    toggleProfession(index) {
      const i = this.openProfessions.indexOf(index)
      if (i > -1) {
        this.openProfessions.splice(i, 1)
      } else {
        this.openProfessions.push(index)
      }
    },
    toggleStep(index) {
      const i = this.openSteps.indexOf(index)
      if (i > -1) {
        this.openSteps.splice(i, 1)
      } else {
        this.openSteps.push(index)
      }
    },
    scrollToProfessions() {
      this.$refs.professionsSection.scrollIntoView({ behavior: 'smooth' })
    },
  },
}
</script>

<style scoped>
/* Общие стили */
.admission-container {
  max-width: 1100px;
  margin: 0 auto;
  padding: 0 15px 40px;
  font-family: 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue',
    sans-serif;
  color: #2c3e50;
  line-height: 1.6;
}

/* Баннер */
.top-banner {
  width: 100%;
  height: 300px;
  overflow: hidden;
  position: relative;
  margin-bottom: 40px;
  border-radius: 0 0 20px 20px;
}

.banner-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}

/* Заголовки секций */
.section-title {
  font-size: 2rem;
  font-weight: 700;
  color: #2c3e50;
  margin-bottom: 10px;
  text-align: center;
}

.section-subtitle {
  font-size: 1.1rem;
  color: #7f8c8d;
  text-align: center;
  margin-bottom: 30px;
  font-weight: 500;
}

/* Таблица специальностей */
.professions-table {
  background: white;
  border-radius: 16px;
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.08);
  overflow: hidden;
  margin-bottom: 50px;
  padding: 20px 0;
}

.profession-item {
  margin-bottom: 5px;
}

.table-header {
  display: flex;
  background: #f8f9fa;
  color: #34495e;
  padding: 15px 20px;
  font-weight: 700;
  font-size: 1rem;
  border-bottom: 1px solid #e0e0e0;
}

.table-row {
  display: flex;
  padding: 15px 20px;
  cursor: pointer;
  align-items: center;
  transition: all 0.2s ease;
  position: relative;
}

.table-row:hover {
  background: #f8fafc;
}

.table-row.active {
  background: #f0f7ff;
}

.table-row.active::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 20px;
  right: 20px;
  height: 1px;
  background: #e0e0e0;
}

.icon-col {
  width: 60px;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}

.profession-icon {
  width: 50px;
  height: 50px;
  border-radius: 50%;
  overflow: hidden;
  border: 2px solid #ecf0f1;
  background: #f8f9fa;
}

.icon-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.name-col {
  flex: 3;
  padding-right: 15px;
}

.code {
  font-weight: 700;
  color: #c43e3e;
  font-size: 0.9rem;
  margin-bottom: 3px;
}

.name {
  font-weight: 600;
  font-size: 1.1rem;
  margin-bottom: 5px;
}

.specialization {
  font-size: 0.9rem;
  color: #7f8c8d;
  font-style: italic;
}

.full-time-col,
.part-time-col {
  flex: 2;
  font-size: 0.9rem;
}

.study-type {
  font-weight: 600;
  color: #34495e;
  margin-bottom: 5px;
  font-size: 0.85rem;
}

.grades {
  display: flex;
  flex-direction: column;
  gap: 5px;
}

.grade-9,
.grade-11 {
  display: flex;
  align-items: center;
  gap: 5px;
}

.label {
  color: #7f8c8d;
  font-size: 0.8rem;
  min-width: 35px;
}

.budget {
  color: #27ae60;
  font-weight: 600;
}

.paid {
  color: #e74c3c;
  font-weight: 600;
}

/* Описание специальности */
.profession-description {
  padding: 20px;
  background: #f8fafc;
  font-size: 0.95rem;
}

.profession-description h3 {
  margin-top: 0;
  margin-bottom: 10px;
  font-size: 1.3rem;
  color: #2c3e50;
}

.total-places {
  font-size: 0.95rem;
  color: #7f8c8d;
  margin-bottom: 15px;
}

.profession-description p {
  margin-bottom: 15px;
}

.advantages {
  margin-top: 15px;
}

.advantage {
  display: flex;
  align-items: center;
  margin-bottom: 8px;
}

.advantage-icon {
  margin-right: 10px;
  flex-shrink: 0;
}

/* Шаги поступления */
.admission-steps {
  background: white;
  border-radius: 16px;
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.08);
  padding: 30px;
}

.steps-container {
  display: flex;
  flex-direction: column;
  gap: 15px;
}

.step {
  border-radius: 10px;
  overflow: hidden;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
  transition: all 0.3s ease;
}

.step-header {
  display: flex;
  align-items: center;
  padding: 15px 20px;
  background: #f8f9fa;
  cursor: pointer;
  user-select: none;
}

.step-number {
  width: 30px;
  height: 30px;
  background: #c43e3e;
  color: white;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 700;
  margin-right: 15px;
  flex-shrink: 0;
}

.step-header h3 {
  margin: 0;
  font-size: 1.1rem;
  font-weight: 600;
  color: #2c3e50;
  flex-grow: 1;
}

.arrow {
  width: 24px;
  height: 24px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #7f8c8d;
  transition: transform 0.3s ease;
}

.arrow.open {
  transform: rotate(180deg);
}

.step-content {
  padding: 15px 20px;
  background: white;
  font-size: 0.95rem;
}

.step-content p {
  margin-bottom: 15px;
}

.step-content ul {
  margin: 0 0 15px 0;
  padding-left: 20px;
}

.step-content li {
  margin-bottom: 8px;
  position: relative;
  padding-left: 25px;
}

.list-icon {
  position: absolute;
  left: 0;
  top: 3px;
}

.step-notes {
  background: #fff9e6;
  padding: 12px 15px;
  border-radius: 8px;
  display: flex;
  align-items: flex-start;
  gap: 10px;
}

.note-icon {
  flex-shrink: 0;
  margin-top: 2px;
}

.step-notes p {
  margin: 0;
  color: #e67e22;
  font-weight: 500;
}

/* Анимации */
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.3s ease, max-height 0.3s ease;
}
.fade-enter-from,
.fade-leave-to {
  opacity: 0;
  max-height: 0;
}
.fade-enter-to,
.fade-leave-from {
  opacity: 1;
  max-height: 1000px;
}

.slide-enter-active,
.slide-leave-active {
  transition: all 0.3s ease;
  max-height: 500px;
  overflow: hidden;
}
.slide-enter-from,
.slide-leave-to {
  max-height: 0;
  opacity: 0;
  transform: translateY(-10px);
}

/* Адаптив для мобильных */
@media (max-width: 768px) {
  .top-banner {
    height: 200px;
    margin-bottom: 30px;
    border-radius: 0;
  }

  .section-title {
    font-size: 1.6rem;
  }

  .section-subtitle {
    font-size: 1rem;
  }

  .table-header {
    display: none;
  }

  .table-row {
    flex-wrap: wrap;
    padding: 15px;
    position: relative;
  }

  .icon-col {
    position: absolute;
    left: 15px;
    top: 15px;
    width: 40px;
  }

  .profession-icon {
    width: 40px;
    height: 40px;
  }

  .name-col {
    flex: 1 1 100%;
    padding-left: 50px;
    margin-bottom: 10px;
  }

  .full-time-col,
  .part-time-col {
    flex: 1 1 50%;
    padding: 5px;
  }

  .study-type {
    font-size: 0.8rem;
    margin-bottom: 3px;
  }

  .grades {
    gap: 3px;
  }

  .label {
    font-size: 0.75rem;
    min-width: 30px;
  }

  .profession-description {
    padding: 15px;
  }

  .admission-steps {
    padding: 20px 15px;
  }

  .step-header {
    padding: 12px 15px;
  }

  .step-header h3 {
    font-size: 1rem;
  }

  .step-content {
    padding: 12px 15px;
  }

  .step-content li {
    padding-left: 20px;
  }

  .list-icon {
    width: 14px;
    height: 14px;
    top: 4px;
  }
}

@media (max-width: 480px) {
  .full-time-col,
  .part-time-col {
    flex: 1 1 100%;
  }

  .part-time-col {
    margin-top: 10px;
  }
}
</style>
