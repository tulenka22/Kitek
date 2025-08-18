<template>
  <block-ab title="Конкурсы, олимпиады, конференции">
    <EntitiesImgScreen :instance="visible" :images="imagesContests" :separatePage="false" />
    <SplitLinks :links="links" />
    <p class="ab__p" @click=";(general_education = !general_education), (visible = false)">
      <icon-wrapper class="icon-tap" width="20" height="24"><icon-tapclick /></icon-wrapper
      ><b>ОЛИМПИАДЫ ПО ОБЩЕОБРАЗОВАТЕЛЬНЫМ ДИСЦИПЛИНАМ ОБРАЗОВАТЕЛЬНЫМ ДИСЦИПЛИНАМ </b>
    </p>
    <ul class="ab__list" v-show="general_education">
      <li>
        <a class="ab__link" target="_blank" rel="nofollow" href="http://профконкурс.рф/index/0-195"
          >Всероссийская олимпиада по истории Сталинградской битвы "Ты победил, Великий
          Сталинград"</a
        >
      </li>
      <li>
        <a class="ab__link" target="_blank" rel="nofollow" href="http://профконкурс.рф/index/0-78"
          >Всероссийская олимпиада "Эпоха комсомола в истории страны"</a
        >
      </li>
      <li>
        <a class="ab__link" target="_blank" rel="nofollow" href="http://профконкурс.рф/index/0-182"
          >Всероссийская олимпиада, посвященная жизни и творчеству Николая Алексеевича Некрасова</a
        >
      </li>
      <li>
        <a class="ab__link" target="_blank" rel="nofollow" href="http://профконкурс.рф/index/0-177"
          >Всероссийская олимпиада, посвященная жизни и творчеству Фёдора Михайловича
          Достоевского</a
        >
      </li>
      <li>
        <a class="ab__link" target="_blank" rel="nofollow" href="http://профконкурс.рф/index/0-105"
          >Всероссийская олимпиада "Творчество А.С. Пушкина"</a
        >
      </li>
      <li>
        <a class="ab__link" target="_blank" rel="nofollow" href="http://профконкурс.рф/index/0-70"
          >Всероссийская олимпиада "Творчество И.С. Тургенева"</a
        >
      </li>
      <li>
        <a class="ab__link" target="_blank" rel="nofollow" href="http://профконкурс.рф/index/0-94"
          >Всероссийская олимпиада по литературе</a
        >
      </li>
      <li>
        <a class="ab__link" target="_blank" rel="nofollow" href="http://профконкурс.рф/index/0-48"
          >Всероссийская олимпиада по русскому языку</a
        >
      </li>
      <li>
        <a class="ab__link" target="_blank" rel="nofollow" href="http://профконкурс.рф/index/0-178"
          >Всероссийская олимпиада по истории "Холодная война"</a
        >
      </li>
      <li>
        <a class="ab__link" target="_blank" rel="nofollow" href="http://профконкурс.рф/index/0-138"
          >Всероссийская олимпиада по истории “Россия в начале XX века”</a
        >
      </li>
      <li>
        <a class="ab__link" target="_blank" rel="nofollow" href="http://профконкурс.рф/index/0-29">
          Всероссийская олимпиада "Русь-сила непобедимая"</a
        >
      </li>
      <li>
        <a class="ab__link" target="_blank" rel="nofollow" href="http://профконкурс.рф/index/0-154">
          Всероссийская олимпиада по дисциплине "Естествознание"</a
        >
      </li>
      <li>
        <a class="ab__link" target="_blank" rel="nofollow" href="http://профконкурс.рф/index/0-153">
          Всероссийская олимпиада по Астрономии</a
        >
      </li>
      <li>
        <a class="ab__link" target="_blank" rel="nofollow" href="http://профконкурс.рф/index/0-53">
          Всероссийская олимпиада по обществознанию</a
        >
      </li>
      <li>
        <a class="ab__link" target="_blank" rel="nofollow" href="http://профконкурс.рф/index/0-15">
          Всероссийская олимпиада по химии</a
        >
      </li>
      <li>
        <a class="ab__link" target="_blank" rel="nofollow" href="http://профконкурс.рф/index/0-109">
          Международная олимпиада,посвященная Периодической таблице химических элементов</a
        >
      </li>
      <li>
        <a class="ab__link" target="_blank" rel="nofollow" href="http://профконкурс.рф/index/0-34">
          Всероссийская олимпиада по физике</a
        >
      </li>
      <li>
        <a class="ab__link" target="_blank" rel="nofollow" href="http://профконкурс.рф/index/0-64">
          Всероссийская олимпиада по английскому языку</a
        >
      </li>
      <li>
        <a class="ab__link" target="_blank" rel="nofollow" href="http://профконкурс.рф/index/0-69">
          Всероссийская олимпиада по философии</a
        >
      </li>
      <li>
        <a class="ab__link" target="_blank" rel="nofollow" href="http://профконкурс.рф/index/0-16">
          Всероссийская олимпиада "География"</a
        >
      </li>
      <li>
        <a class="ab__link" target="_blank" rel="nofollow" href="http://профконкурс.рф/index/0-27">
          Всероссийская олимпиада по биологии</a
        >
      </li>
      <li>
        <a class="ab__link" target="_blank" rel="nofollow" href="http://профконкурс.рф/index/0-21">
          Всероссийская олимпиада по математике</a
        >
      </li>
      <li>
        <a class="ab__link" target="_blank" rel="nofollow" href="http://профконкурс.рф/index/0-102">
          Всероссийская олимпиада "Физическая культура"</a
        >
      </li>
      <li>
        <a class="ab__link" target="_blank" rel="nofollow" href="http://профконкурс.рф/index/0-40">
          Всероссийская олимпиада по экологии</a
        >
      </li>
      <li>
        <a class="ab__link" target="_blank" rel="nofollow" href="http://профконкурс.рф/index/0-23">
          Всероссийская олимпиада "Информатика и ИКТ"</a
        >
      </li>
      <li>
        <a class="ab__link" target="_blank" rel="nofollow" href="http://профконкурс.рф/index/0-26">
          Всероссийская олимпиада по "ОБЖ"</a
        >
      </li>
    </ul>
    <p
      class="ab__p"
      @click=";(professional_education = !professional_education), (visible = false)">
      <icon-wrapper class="icon-tap" width="20" height="24"><icon-tapclick /></icon-wrapper
      ><b>ОЛИМПИАДЫ ПО ОБЩЕПРОФЕССИОНАЛЬНЫМ ДИСЦИПЛИНАМ</b>
    </p>
    <ul class="ab__list" v-show="professional_education">
      <li>
        <a class="ab__link" target="_blank" rel="nofollow" href="http://профконкурс.рф/index/0-168"
          >Всероссийская олимпиада по "Психологии общения"</a
        >
      </li>
      <li>
        <a class="ab__link" target="_blank" rel="nofollow" href="http://профконкурс.рф/index/0-63">
          Всероссийская олимпиада по культурологии</a
        >
      </li>
      <li>
        <a class="ab__link" target="_blank" rel="nofollow" href="http://профконкурс.рф/index/0-104">
          Всероссийская олимпиада "Основы микробиологии"</a
        >
      </li>
      <li>
        <a class="ab__link" target="_blank" rel="nofollow" href="http://профконкурс.рф/index/0-142">
          Всероссийская олимпиада "Основы предпринимательства"</a
        >
      </li>
      <li>
        <a class="ab__link" target="_blank" rel="nofollow" href="http://профконкурс.рф/index/0-173">
          Всероссийская олимпиада "Проектирование профессиональной карьеры"</a
        >
      </li>
      <li>
        <a class="ab__link" target="_blank" rel="nofollow" href="http://профконкурс.рф/index/0-24">
          Всероссийская олимпиада по экономике</a
        >
      </li>
      <li>
        <a class="ab__link" target="_blank" rel="nofollow" href="http://профконкурс.рф/index/0-122">
          Всероссийская олимпиада "Экономика организации"</a
        >
      </li>
      <li>
        <a class="ab__link" target="_blank" rel="nofollow" href="http://профконкурс.рф/index/0-144">
          Всероссийская олимпиада по экономической географии</a
        >
      </li>
      <li>
        <a class="ab__link" target="_blank" rel="nofollow" href="http://профконкурс.рф/index/0-59">
          Всероссийская олимпиада "Метрология и стандартизация"</a
        >
      </li>
      <li>
        <a class="ab__link" target="_blank" rel="nofollow" href="http://профконкурс.рф/index/0-58">
          Всероссийская олимпиада по специальности "Коммерция"</a
        >
      </li>
      <li>
        <a class="ab__link" target="_blank" rel="nofollow" href="http://профконкурс.рф/index/0-145">
          Всероссийская олимпиада "Правовое обеспечение профессиональной деятельности"</a
        >
      </li>
      <li>
        <a class="ab__link" target="_blank" rel="nofollow" href="http://профконкурс.рф/index/0-103">
          Всероссийская олимпиада "Гражданское право"</a
        >
      </li>
      <li>
        <a class="ab__link" target="_blank" rel="nofollow" href="http://профконкурс.рф/index/0-108">
          Всероссийская олимпиада "Конституционное право"</a
        >
      </li>
      <li>
        <a class="ab__link" target="_blank" rel="nofollow" href="http://профконкурс.рф/index/0-113">
          Всероссийская олимпиада “Административное право”</a
        >
      </li>
      <li>
        <a class="ab__link" target="_blank" rel="nofollow" href="http://профконкурс.рф/index/0-17">
          Всероссийская олимпиада по праву</a
        >
      </li>
      <li>
        <a class="ab__link" target="_blank" rel="nofollow" href="http://профконкурс.рф/index/0-119">
          Всероссийская олимпиада по информационным технологиям</a
        >
      </li>
      <li>
        <a class="ab__link" target="_blank" rel="nofollow" href="http://профконкурс.рф/index/0-158">
          Всероссийская олимпиада по Инженерной компьютерной графике</a
        >
      </li>
      <li>
        <a class="ab__link" target="_blank" rel="nofollow" href="http://профконкурс.рф/index/0-147">
          Всероссийская олимпиада "Операционные системы и среды"</a
        >
      </li>
      <li>
        <a class="ab__link" target="_blank" rel="nofollow" href="http://профконкурс.рф/index/0-110">
          Всероссийская олимпиада по экологическим основам природопользования</a
        >
      </li>
      <li>
        <a class="ab__link" target="_blank" rel="nofollow" href="http://профконкурс.рф/index/0-77">
          Всероссийская олимпиада "Гостиничный сервис"</a
        >
      </li>
      <li>
        <a class="ab__link" target="_blank" rel="nofollow" href="http://профконкурс.рф/index/0-98">
          Всероссийская олимпиада "Товароведение продовольственных товаров"</a
        >
      </li>
      <li>
        <a class="ab__link" target="_blank" rel="nofollow" href="http://профконкурс.рф/index/0-76">
          Всероссийская олимпиада "Товароведение непродовольственных товаров"</a
        >
      </li>
      <li>
        <a class="ab__link" target="_blank" rel="nofollow" href="http://профконкурс.рф/index/0-45">
          Всероссийская олимпиада "Бухгалтерский учёт"</a
        >
      </li>
      <li>
        <a class="ab__link" target="_blank" rel="nofollow" href="http://профконкурс.рф/index/0-179">
          Всероссийская олимпиада по дисциплине "Аудит"</a
        >
      </li>
      <li>
        <a class="ab__link" target="_blank" rel="nofollow" href="http://профконкурс.рф/index/0-85">
          Всероссийская олимпиада "Финансы, денежное обращение и кредит"</a
        >
      </li>
    </ul>
    <p class="ab__p" @click=";(thematic_olympiads = !thematic_olympiads), (visible = false)">
      <icon-wrapper class="icon-tap" width="20" height="24"><icon-tapclick /></icon-wrapper
      ><b>ТЕМАТИЧЕСКИЕ ОЛИМПИАДЫ, ВСЕРОССИЙСКИЕ ВИКТОРИНЫ И ТЕСТЫ</b>
    </p>
    <ul class="ab__list" v-show="thematic_olympiads">
      <li>
        <a class="ab__link" target="_blank" rel="nofollow" href="http://профконкурс.рф/index/0-164"
          >Всероссийская олимпиада "Александр Невский - славное имя Земли Русской"</a
        >
      </li>
      <li>
        <a class="ab__link" target="_blank" rel="nofollow" href="http://профконкурс.рф/index/0-30"
          >Всероссийская викторина "Единство России"</a
        >
      </li>
      <li>
        <a class="ab__link" target="_blank" rel="nofollow" href="http://профконкурс.рф/index/0-143"
          >Всероссийская олимпиада "Россия - Родина моя"</a
        >
      </li>
      <li>
        <a class="ab__link" target="_blank" rel="nofollow" href="http://профконкурс.рф/index/0-139">
          Всероссийская олимпиада "Цифровая компетентность как алгоритм жизненных навыков"</a
        >
      </li>
      <li>
        <a class="ab__link" target="_blank" rel="nofollow" href="http://профконкурс.рф/index/0-72">
          Всероссийская олимпиада, посвященная "Победе в Великой Отечественной войне"</a
        >
      </li>
      <li>
        <a class="ab__link" target="_blank" rel="nofollow" href="http://профконкурс.рф/index/0-131">
          Всероссийская олимпиада "Пётр I - император великой России"</a
        >
      </li>
      <li>
        <a class="ab__link" target="_blank" rel="nofollow" href="http://профконкурс.рф/index/0-130">
          Всероссийская олимпиада, посвященная полководцу Александру Васильевичу Суворову</a
        >
      </li>
      <li>
        <a class="ab__link" target="_blank" rel="nofollow" href="http://профконкурс.рф/index/0-44">
          Всероссийская викторина "Развитие движения WorldSkills в России"</a
        >
      </li>
      <li>
        <a class="ab__link" target="_blank" rel="nofollow" href="http://профконкурс.рф/index/0-92">
          Международная олимпиада "История Профтехобразования"</a
        >
      </li>
      <li>
        <a class="ab__link" target="_blank" rel="nofollow" href="http://профконкурс.рф/index/0-90">
          Всероссийская олимпиада "История создания Рабоче-крестьянской Красной армии"</a
        >
      </li>
      <li>
        <a class="ab__link" target="_blank" rel="nofollow" href="http://профконкурс.рф/index/0-83">
          Всероссийская олимпиада "Информационная безопасность в интернете"</a
        >
      </li>
      <li>
        <a class="ab__link" target="_blank" rel="nofollow" href="http://профконкурс.рф/index/0-74">
          Всероссийская олимпиада "Финансовая грамотность"</a
        >
      </li>
      <li>
        <a class="ab__link" target="_blank" rel="nofollow" href="http://профконкурс.рф/index/0-20">
          Всероссийская викторина "День космонавтики"</a
        >
      </li>
    </ul>
    <p class="ab__p" @click=";(photo_exhibition = !photo_exhibition), (visible = false)">
      <icon-wrapper class="icon-tap" width="20" height="24"><icon-tapclick /></icon-wrapper
      ><b>ФОТОВЫСТАВКА «КРАСОТА ПРИРОДЫ РОДНОЙ ОБЛАСТИ/ГОРОДА»</b>
    </p>
    <div v-show="photo_exhibition">
      <p class="ab__p">
        Мы искали таланты и нашли их! В нашем колледже учатся те, кто не только умеет делать
        высокохудожественные фото, но видеть красоту вокруг себя. Как однажды сказал Пауло Коэльо:
        "Если ты способен видеть прекрасное, то только потому, что носишь прекрасное внутри себя.
        Ибо мир подобен зеркалу, в котором каждый видит собственное отражение."
      </p>
      <p class="ab__p">
        Это прекрасное было увидено в окружающей нас природе, в тех местах, где бываем мы Все и не
        замечаем, как они красивы. Давайте вместе ещё раз посмотрим на красоту окружающего нас
        пространства, на наш общий «дом»!
      </p>
      <div class="ab__photos">
        <img
          v-for="img of [1, 2, 3, 4, 5, 6]"
          :key="img"
          class="ab__photo"
          :src="`/img/contests/w${img}.jpg`"
          alt="Photography"
          v-on:click="visible = !visible" />
      </div>
      <div class="ab__photos">
        <img
          v-for="img of [1, 2, 3]"
          :key="img"
          class="ab__photo-vertical"
          :src="`/img/contests/v${img}.jpg`"
          alt="Photography"
          v-on:click="visible = !visible" />
      </div>
      <div class="ab__photos">
        <img
          v-for="img of [1, 2, 3]"
          :key="img"
          class="ab__photo-square"
          :src="`/img/contests/s${img}.jpg`"
          alt="Photography"
          v-on:click="visible = !visible" />
      </div>
    </div>

    <p class="ab__p" @click=";(kk = !kk), (visible = false)">
      <icon-wrapper class="icon-tap" width="20" height="24"><icon-tapclick /></icon-wrapper
      ><b>"КОНКУРСЫ ПРОФЕССИОНАЛЬНОГО МАСТЕРСТВА"</b>
    </p>
    <div v-show="kk">
      <block-ab title="Профессионалы! Мастера! Чемпионы!">
        <p class="ab__p">
          Важнейшей задачей системы среднего профессионального образования является совершенствование
          подготовки специалистов и повышение уровня профессиональных знаний, формирование у студентов
          системного мышления, ориентированного на эффективное использования приобретенных навыков в
          будущей практической деятельности. Решение поставленной задачи достигается различными
          дидактическими приемами, среди которых одно из важных мест занимает проведение и участие в
          конкурсах и чемпионатах профессионального мастерства.
        </p>
        <p class="ab__p">
          Важнейшей задачей системы среднего профессионального образования является совершенствование
          подготовки специалистов и повышение уровня профессиональных знаний, формирование у студентов
          системного мышления, ориентированного на эффективное использования приобретенных навыков в
          будущей практической деятельности. Решение поставленной задачи достигается различными
          дидактическими приемами, среди которых одно из важных мест занимает проведение и участие в
          конкурсах и чемпионатах профессионального мастерства.
        </p>
        <p class="ab__p">
          В БПОУ «КИТЭК» сложилась многолетняя практика проведения конкурсов профессионального
          мастерства. Среди них можно назвать следующие:
        </p>
        <p class="ab__p">
          - Конкурс профессионального мастерства для преподавателей и мастеров производственного
          обучения по компетенции «Поварское дело», в котором принимают участие преподаватели колледжей
          и техникумов Омска и Омской области. Работу конкурсантов оценивают опытные шеф-повара
          ресторанов города. Конкурс проходит под эгидой Омской областной общественной организации
          «Ассоциация Омских Кулинаров».
        </p>
        <p class="ab__p">- Открытый кулинарный чемпионат «CHEFS TEAM FEST ОМСК».</p>
        <p class="ab__p">
          - Конкурс профессионального мастерства обучающихся БПОУ «КИТЭК» по специальностям 38.02.05
          Товароведение и экспертиза качества потребительских товаров, 38.02.04 Коммерция на базе ООО
          «Лента» среди обучающихся колледжей и техникумов города Омска.
        </p>
        <p class="ab__p">
          - Открытый чемпионат профессионального мастерства Бариста среди студентов 3 и 4 курсов
          колледжа, обучающихся по специальностям «Гостиничное дело» и «Поварское и кондитерское дело».
          Чемпионат проходит в несколько этапов: в первом - участникам необходимо было приготовить кофе
          экспрессо, на втором этапе - необходимо приготовить кофе капучино. Затем, финалистам конкурса
          был предоставлен простор для фантазии приготовления напитка на основе кофе экспрессо. Ребята
          показали мастерство при работе на профессиональной кофемашине и кофемолке. Продемонстрировали
          знания в области работы бариста.
        </p>
        <p class="ab__p">
          - Открытый конкурс профессионального мастерства «Администратор отеля» среди студентов 3 курса
          колледжа.
        </p>
        <p class="ab__p">
          Обучающиеся колледжа принимают активное участие в мероприятиях городского и областного
          уровней: Региональный чемпионат профессионального мастерства «Профессионалы»; Региональный
          чемпионат по профессиональному мастерству среди инвалидов и лиц с ограниченными возможностями
          здоровья «Абилимпикс».
        </p>
        <p class="ab__p">
          - Работа «Полевой кухни» на общегородских мероприятиях, посвященных празднованию годовщины
          Победы в парке Победы.
        </p>
        <p class="ab__p">
          Отдельно хочется отметить конкурсы, проходящие под эгидой института развития профессионального
          образования, в которых можно принять участие:
        </p>
        <p class="ab__p">
          Международный конкурс творческих студенческих проектов антикоррупционной направленности
          проводится с целью привлечения внимания общественности к проблеме коррупции, поддержки
          творческих инициатив молодежи в создании социальных антикоррупционных проектов в
          образовательных организациях, реализующих образовательные программы среднего профессионального
          образования
          <p style="color: rgb(124, 165, 255)">
            <a href="https://firpo.ru/activities/contests/mezhdunarodnyy-konkurs-tvorcheskih-studencheskih-proektov-antikorruptsionnoy-napravlennosti.html">ссылка</a>
        </p>

        </p>
        <p class="ab__p">
          Всероссийский конкурс проектов «История профессии в моей семье: суперпрофессиональная семья»
          способствует популяризации профессиональных династий, развитию преемственности семейных
          трудовых традиций, укреплению значимости института семьи и семейных ценностей, повышению
          престижа рабочих профессий и содействует укреплению авторитета человека труда
          
          <p style="color: rgb(124, 165, 255)">
            <a href="https://firpo.ru/activities/contests/vserossiyskiy-konkurs-proektov-istoriya-professii-v-moey-seme-superprofessionalnaya-semya-1.html">ссылка</a>
        </p>
        </p>
      </block-ab>
      
    </div>
  </block-ab>
</template>

<script>
import { createLink } from '~/core/helpers/link'
export default {
  data() {
    return {
      kk: false,
      general_education: false,
      professional_education: false,
      thematic_olympiads: false,
      photo_exhibition: false,
      visible: false,
      visiblev: false,
      visiblek: false,
      imagesContests: [
        '/img/contests/w1.jpg',
        '/img/contests/w2.jpg',
        '/img/contests/w3.jpg',
        '/img/contests/w4.jpg',
        '/img/contests/w5.jpg',
        '/img/contests/w6.jpg',
        '/img/contests/v1.jpg',
        '/img/contests/v2.jpg',
        '/img/contests/v3.jpg',
        '/img/contests/s1.jpg',
        '/img/contests/s2.jpg',
        '/img/contests/s3.jpg',
      ],
      links: [
        createLink(
          'http://xn--j1aaicbdhfjsg.xn--p1ai/board/',
          'Профконкурс - молодёжная редакция профобразования'
        ),
        createLink(
          'http://проф-обр.рф/news/2023-01-22-2462',
          'Всероссийский конкурсно-образовательный марафон «Наставник- мастер своего дела» '
        ),
        createLink(
          'http://профконкурс.рф/stuff/32-1-0-412',
          'Всероссийский конкурс эссе для студентов и педагогов СПО "Мой выбор — Профобразование"'
        ),
        createLink(
          'http://профконкурс.рф/board/21-1-0-644',
          'VI-Всероссийский фестиваль творческих работ обучающихся, посвященный Победе в Великой Отечественной войне "Никто не забыт и ничто не забыто"'
        ),
        createLink(
          'http://профконкурс.рф/news/2021-10-01-323',
          'Международный фотоконкурс для преподавателей и студентов СПО "PROFKADR"'
        ),
      ],
    }
  },
}
</script>

<style scoped lang="scss">
.ab {
  &__p {
    cursor: pointer;
  }
  &__photos {
    margin: 32px 0;
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
    gap: 16px;
    max-width: 60vw;
  }
  &__photo {
    width: auto;
    height: 200px;
    margin: auto;
    object-fit: cover;
    cursor: pointer;
    &-vertical {
      width: auto;
      height: 300px;
      margin: auto;
      cursor: pointer;
    }
    &-square {
      width: 350px;
      height: 300px;
      margin: auto;
      cursor: pointer;
    }
  }
}
</style>
