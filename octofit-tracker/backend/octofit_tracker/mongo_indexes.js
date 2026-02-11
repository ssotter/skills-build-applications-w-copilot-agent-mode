// Script para criar índice único no campo email da coleção users
// Execute no mongosh conectado ao octofit_db

db.users.createIndex({ "email": 1 }, { unique: true })
