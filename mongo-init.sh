set -e

mongo <<EOF
db = db.getSiblingDB('$MONGO_DB')

db.createUser({
  user: '$MONGO_API_USER',
  pwd: '$MONGO_API_PASS',
  roles: [{ role: 'readWrite', db: '$MONGO_DB' }],
});
db.createCollection('$MONGO_COLLECTION')

EOF