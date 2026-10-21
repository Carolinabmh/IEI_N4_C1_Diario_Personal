-- Crear la base de datos del diario personal
CREATE DATABASE IF NOT EXISTS diario_personal_v2
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

-- Crear un usuario específico para la aplicación
CREATE USER IF NOT EXISTS 'diario_app'@'localhost'
IDENTIFIED BY 'CAMBIAR_POR_UNA_CONTRASENA_SEGURA';

-- Otorgar permisos sobre la base de datos
GRANT ALL PRIVILEGES ON diario_personal_v2.*
TO 'diario_app'@'localhost';

-- Actualizar los permisos
FLUSH PRIVILEGES;