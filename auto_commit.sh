#!/bin/bash

# Set your Gemini API Key
API_KEY="AIzaSyC3zyEO00wXlFyUPZImANcGwtn3vFLUYEI"

# Ambil perubahan yang di-stage
DIFF=$(git diff --cached)

# Buat prompt
PROMPT="Generate a concise and meaningful git commit message for this diff:\n\n$DIFF"

# Kirim ke Gemini
RESPONSE=$(curl -s -X POST \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $API_KEY" \
  -d "{
        'contents': [
          { 'parts': [ { 'text': \"$PROMPT\" } ] }
        ]
      }" \
  "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key=$API_KEY")

# Ambil hasil commit message dari JSON
MESSAGE=$(echo "$RESPONSE" | jq -r '.candidates[0].content.parts[0].text')

# Commit
git commit -m "$MESSAGE"
echo "Proses selesai."
read -p "Tekan Enter untuk keluar..."
