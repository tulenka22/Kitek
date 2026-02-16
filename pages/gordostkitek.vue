<template>
  <block-ab title="">
    <div class="pride-container">
      <header>
        <h1>Гордость КИТЭК</h1>
        <p class="subtitle">
          Узнайте мнение тех, кто уже учится и преподает в нашем колледже. Реальные истории и
          впечатления от образовательного процесса.
        </p>
      </header>

      <div class="tabs">
        <button
          class="tab-btn"
          :class="{ active: activeTab === 'students', pulse: activeTab === 'students' }"
          @click="setActiveTab('students')">
          <i class="fas fa-user-graduate"></i> Отзывы студентов
        </button>
        <button
          class="tab-btn"
          :class="{ active: activeTab === 'teachers', pulse: activeTab === 'teachers' }"
          @click="setActiveTab('teachers')">
          <i class="fas fa-chalkboard-teacher"></i> Отзывы преподавателей
        </button>
      </div>

      <div class="cards-container">
        <!-- Студенты -->
        <div
          v-for="(student, index) in students"
          :key="'student-' + index"
          class="card"
          :class="{ 'fade-in': activeTab === 'students' }"
          v-show="activeTab === 'students'">
          <div class="video-container">
            <video
              ref="videoPlayer"
              controls
              muted
              playsinline
              class="video-player"
              :poster="student.posterUrl"
              @click.stop>
              <source :src="student.videoUrl" type="video/mp4" />
              Ваш браузер не поддерживает видео.
            </video>
            <div
              v-if="!student.videoPlaying"
              class="play-overlay"
              @click="playVideo(student, index)">
              <i class="fas fa-play-circle"></i>
              <h3>Интервью со {{ student.gender === 'female' ? 'студенткой' : 'студентом' }}</h3>
            </div>
          </div>
          <div class="card-content">
            <div class="quote-icon">
              <i class="fas fa-quote-left"></i>
            </div>
            <h2 class="name">{{ student.name }}</h2>
            <span class="years">{{ student.years }}</span>
            <p class="description">{{ student.description }}</p>
            <div class="university">
              <i class="fas fa-university"></i>
              <span>{{ student.university }}</span>
            </div>
          </div>
        </div>

        <!-- Преподаватели -->
        <div
          v-for="(teacher, index) in teachers"
          :key="'teacher-' + index"
          class="card"
          :class="{ 'fade-in': activeTab === 'teachers' }"
          v-show="activeTab === 'teachers'">
          <div class="video-container">
            <video
              ref="videoPlayer"
              controls
              muted
              playsinline
              class="video-player"
              :poster="teacher.posterUrl"
              @click.stop>
              <source :src="teacher.videoUrl" type="video/mp4" />
              Ваш браузер не поддерживает видео.
            </video>
            <div
              v-if="!teacher.videoPlaying"
              class="play-overlay"
              @click="playVideo(teacher, index)">
              <i class="fas fa-play-circle"></i>
              <h3>Интервью с преподавателем</h3>
            </div>
          </div>
          <div class="card-content">
            <div class="quote-icon">
              <i class="fas fa-quote-left"></i>
            </div>
            <h2 class="name">{{ teacher.name }}</h2>
            <span class="years">{{ teacher.years }}</span>
            <p class="description">{{ teacher.description }}</p>
            <div class="university">
              <i class="fas fa-university"></i>
              <span>{{ teacher.university }}</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </block-ab>
</template>

<script>
export default {
  name: 'PrideKitEK',
  data() {
    return {
      activeTab: 'students',
      students: [
        {
          name: 'Беляевская Снежана',
          years: 'Год выпуска 2025',
          description: '43 ПКД',
          university: 'Колледж КИТЭК',
          gender: 'female',
          posterUrl: '/images/video-poster.jpg',
          videoUrl: '/video/stud1.mp4',

          videoPlaying: false,
        },
        {
          name: 'Жукенова Диана',
          years: 'Год выпуска 2025',
          description: '42 ПКД',
          university: 'Колледж КИТЭК',
          gender: 'male',
          videoUrl: '/video/stud2.mp4',
          posterUrl: '/images/video-poster.jpg',
          videoPlaying: false,
        },
        {
          name: 'Колиева Ульяна',
          years: 'Год выпуска 2025',
          description: '41 ИСР',
          university: 'Колледж КИТЭК',
          gender: 'female',
          videoUrl: '/video/stud3.mp4',
          posterUrl: '/images/video-poster.jpg',
          videoPlaying: false,
        },
        {
          name: 'Спирина Софья',
          years: 'Год выпуска 2025',
          description: '31 ТЭ',
          university: 'Колледж КИТЭК',
          gender: 'female',
          videoUrl: '/video/stud4.mp4',
          posterUrl: '/images/video-poster.jpg',
          videoPlaying: false,
        },
      ],
      teachers: [
        {
          name: 'Маслова Надежда Алексеевна',

          description: 'Преподователь',
          university: 'Колледж КИТЭК',
          videoUrl: '/video/prepod1.mp4',
          posterUrl: '/images/video-poster.jpg',
          videoPlaying: false,
        },
        {
          name: 'Малкова Людмила Викторовна',

          description: 'Преподователь',
          university: 'Колледж КИТЭК',
          videoUrl: '/video/prepod2.mp4',
          posterUrl: '/images/video-poster.jpg',
          videoPlaying: false,
        },
        {
          name: 'Петрова Вероника Валерьевна',

          description: 'Преподователь',
          university: 'Колледж КИТЭК',
          videoUrl: '/video/prepod3.mp4',
          posterUrl: '/images/video-poster.jpg',
          videoPlaying: false,
        },
        {
          name: 'Спирина Наталья Алексеевна',

          description: 'Преподователь',
          university: 'Колледж КИТЭК',
          videoUrl: '/video/prepod4.mp4',
          posterUrl: '/images/video-poster.jpg',
          videoPlaying: false,
        },
        {
          name: 'Сулейменова Д.О. Паленая Т.Н. Белан А.С. Зайцева Л.В.',

          description: 'Преподователи',
          university: 'Колледж КИТЭК',
          videoUrl: '/video/prepod5.mp4',
          posterUrl: '/images/video-poster.jpg',
          videoPlaying: false,
        },
        {
          name: 'Воропанова Е.Н.',

          description: 'Преподователь',
          university: 'Колледж КИТЭК',
          videoUrl: '/video/prepod6.mp4',
          posterUrl: '/images/video-poster.jpg',
          videoPlaying: false,
        },
        {
          name: 'Кудинова О.В.',

          description: 'Преподователь',
          university: 'Колледж КИТЭК',
          videoUrl: '/video/prepod7.mp4',
          posterUrl: '/images/video-poster.jpg',
          videoPlaying: false,
        },
        {
          name: 'Павленко А.В.',

          description: 'Преподователь',
          university: 'Колледж КИТЭК',
          videoUrl: '/video/prepod8.mp4',
          posterUrl: '/images/video-poster.jpg',
          videoPlaying: false,
        },
        {
          name: 'Федорова Г.Н. Старостина Н.А. Абилова Т.Н.',

          description: 'Преподователь',
          university: 'Колледж КИТЭК',
          videoUrl: '/video/prepod9.mp4',
          posterUrl: '/images/video-poster.jpg',
          videoPlaying: false,
        },
        {
          name: 'Фурман В.А.',

          description: 'Преподователь',
          university: 'Колледж КИТЭК',
          videoUrl: '/video/prepod10.mp4',
          posterUrl: '/images/video-poster.jpg',
          videoPlaying: false,
        },
        {
          name: 'Хохлов И.И.',

          description: 'Преподователь',
          university: 'Колледж КИТЭК',
          videoUrl: '/video/prepod11.mp4',
          posterUrl: '/images/video-poster.jpg',
          videoPlaying: false,
        },
        {
          name: 'Чукаева Л.И.',

          description: 'Преподователь',
          university: 'Колледж КИТЭК',
          videoUrl: '/video/prepod12.mp4',
          posterUrl: '/images/video-poster.jpg',
          videoPlaying: false,
        },
      ],
    }
  },
  methods: {
    playVideo(item, index) {
      item.videoPlaying = true
      this.$nextTick(() => {
        const videos = this.$refs.videoPlayer
        if (videos && videos[index]) {
          videos[index].play()
        }
      })
    },
    setActiveTab(tab) {
      this.activeTab = tab
    },
  },
}
</script>

<style scoped>
.pride-container {
  max-width: 1400px;
  margin: 0 auto;
  padding: 20px;
  background: white;
  color: #333;
}

header {
  text-align: center;
  padding: 30px 0;
  margin-bottom: 30px;
}

h1 {
  font-size: 2.8rem;
  text-transform: uppercase;
  margin-bottom: 15px;
  color: #222;
  letter-spacing: 1.5px;
  position: relative;
  display: inline-block;
  padding-bottom: 15px;
}

h1:after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 50%;
  transform: translateX(-50%);
  width: 100px;
  height: 4px;
  background: #c43e3e;
  border-radius: 2px;
}

.subtitle {
  font-size: 1.2rem;
  color: #555;
  max-width: 700px;
  margin: 0 auto;
  line-height: 1.6;
}

.tabs {
  display: flex;
  justify-content: center;
  margin-bottom: 40px;
  gap: 20px;
  flex-wrap: wrap;
}

.tab-btn {
  padding: 14px 36px;
  font-size: 1.1rem;
  background: white;
  border: 2px solid #c43e3e;
  color: #c43e3e;
  border-radius: 50px;
  cursor: pointer;
  transition: all 0.3s ease;
  font-weight: 600;
  display: flex;
  align-items: center;
  gap: 10px;
}

.tab-btn:hover {
  background: rgba(196, 62, 62, 0.08);
  transform: translateY(-3px);
}

.tab-btn.active {
  background: #c43e3e;
  color: white;
  box-shadow: 0 4px 15px rgba(196, 62, 62, 0.3);
}

.tab-btn.active.pulse {
  animation: pulse 2s infinite;
}

.cards-container {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
  gap: 30px;
  margin-top: 20px;
}

.card {
  background: white;
  border-radius: 15px;
  overflow: hidden;
  transition: all 0.4s ease;
  border: 1px solid #eee;
  box-shadow: 0 5px 20px rgba(0, 0, 0, 0.05);
  display: flex;
  flex-direction: column;
  height: 100%;
}

.card:hover {
  transform: translateY(-8px);
  box-shadow: 0 12px 25px rgba(0, 0, 0, 0.1);
  border-color: rgba(196, 62, 62, 0.2);
}

.video-container {
  position: relative;
  padding-top: 56.25%; /* 16:9 aspect ratio */
  background: #f1f1f1;
}

.video-player {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  background: #000;
}

.play-overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
  background: rgba(0, 0, 0, 0.2);
  color: white;
  cursor: pointer;
  z-index: 2;
  transition: all 0.3s ease;
}

.play-overlay:hover {
  background: rgba(0, 0, 0, 0.4);
}

.play-overlay i {
  font-size: 4rem;
  color: rgba(255, 255, 255, 0.8);
  text-shadow: 0 2px 10px rgba(0, 0, 0, 0.3);
  margin-bottom: 15px;
  transition: all 0.3s ease;
}

.play-overlay:hover i {
  color: white;
  transform: scale(1.1);
}

.play-overlay h3 {
  font-size: 1.3rem;
  font-weight: 500;
  text-shadow: 0 1px 3px rgba(0, 0, 0, 0.5);
  text-align: center;
  max-width: 90%;
}

.card-content {
  padding: 25px;
  flex-grow: 1;
  display: flex;
  flex-direction: column;
}

.name {
  font-size: 1.6rem;
  margin-bottom: 12px;
  color: #c43e3e;
  font-weight: 700;
}

.years {
  background: rgba(196, 62, 62, 0.08);
  padding: 6px 16px;
  border-radius: 20px;
  display: inline-block;
  margin-bottom: 20px;
  font-weight: 600;
  color: #c43e3e;
  font-size: 0.9rem;
  border: 1px solid rgba(196, 62, 62, 0.15);
}

.description {
  line-height: 1.7;
  flex-grow: 1;
  margin-bottom: 20px;
  color: #555;
  font-size: 1rem;
}

.quote-icon {
  color: rgba(196, 62, 62, 0.3);
  font-size: 1.8rem;
  margin-bottom: 10px;
}

.university {
  display: flex;
  align-items: center;
  padding: 12px 0 0;
  border-top: 1px solid #f0f0f0;
  margin-top: auto;
  color: #777;
  font-size: 0.95rem;
}

.university i {
  margin-right: 10px;
  color: #c43e3e;
}

.fade-in {
  animation: fadeIn 0.8s ease-in;
}

@media (max-width: 900px) {
  .cards-container {
    grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
  }
}

@media (max-width: 768px) {
  .cards-container {
    grid-template-columns: 1fr;
    max-width: 600px;
    margin: 0 auto;
    margin-top: 20px;
  }

  h1 {
    font-size: 2.3rem;
  }

  .tabs {
    flex-direction: column;
    align-items: center;
    gap: 12px;
  }

  .tab-btn {
    width: 100%;
    max-width: 320px;
    justify-content: center;
  }
}

@keyframes pulse {
  0% {
    box-shadow: 0 0 0 0 rgba(196, 62, 62, 0.4);
  }
  70% {
    box-shadow: 0 0 0 12px rgba(196, 62, 62, 0);
  }
  100% {
    box-shadow: 0 0 0 0 rgba(196, 62, 62, 0);
  }
}

@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}
</style>
