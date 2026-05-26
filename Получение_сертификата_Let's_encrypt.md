# Получение сертификата Let's encrypt для Nginx (без Docker)

## Цель работы

Получить и настроить SSL-сертификат Let's Encrypt для веб-сервера Nginx, обеспечив безопасное HTTPS-соединение для домена `melnikno.bizml.ru`.

[Ссылка на скринкаст](https://disk.yandex.ru/i/ZE9YyJvSuwLgmw)

## Выполненные шаги

### 1. Проверка предусловий (Prerequirements)

Перед началом работы убедились, что:

-   Сервер VDS создан в Selectel и доступен по SSH.
-   Доменное имя `melnikno.bizml.ru` находится в собственности.
-   Настроена DNS-запись типа **A**, указывающая на IP сервера: `31.184.254.21`.
-   Веб-сервер Nginx установлен и запущен.

<img width="1442" height="664" alt="image" src="https://github.com/user-attachments/assets/d6aa0160-6b46-442b-92ed-b905df48a96b" />


### 2. Установка Certbot

Для получения сертификата использован официальный клиент Certbot. Установка выполнена через пакетный менеджер `apt`

<img width="1417" height="590" alt="image" src="https://github.com/user-attachments/assets/e58fa16f-457d-41b4-9903-bfab54315ea1" />


<img width="442" height="54" alt="image" src="https://github.com/user-attachments/assets/ddbbe7a2-7715-42c9-8d18-02e511fd5d1c" />

### 3. Обоснование выбора стратегии валидации (ACME challenge)


**Выбранный подход:** HTTP-01 (ACME + Nginx Mode).

**Обоснование:** Этот метод проще в настройке, полностью автоматизирован с помощью плагина Certbot для Nginx и идеально подходит для учебного проекта. Автоматическое перенаправление HTTP → HTTPS повышает безопасность сайта.


### 4. Генерация сертификата и получение ключей

<img width="1054" height="597" alt="image" src="https://github.com/user-attachments/assets/aeae5fd0-e1f9-4ade-8dea-f8fde77f4ad4" />


### 5. Настройка Nginx и символические ссылки

<img width="1286" height="383" alt="image" src="https://github.com/user-attachments/assets/c2da135f-1ce5-4919-b6cb-2a33a92f83ea" />


### Демонстрация работы HTTPS

<img width="1234" height="295" alt="image" src="https://github.com/user-attachments/assets/c9815266-eb2d-41de-a667-67e9e1492aba" />


