from instaloader import Instaloader, Hashtag

def instsearch(hashtag, n,language):
   if hashtag[0] == '#':
      hashtag = hashtag[1:]
   try:
      L = Instaloader()
      hashtag = Hashtag.from_name(L.context, hashtag)
      number = n-1
      link = ''
      for post in hashtag.get_all_posts():
         try:
            number += 1
            if number<(n-1)*10+1:
               continue
         
            link = link + '\n'+('№{} Нікнейм: {}\n{}' if language == 'ukrainian' else '№{} Nickname: {}\n{}').format(number,post.owner_username, 'https://www.instagram.com/p/'+ str(post.shortcode))
            if number == n*10:
               return ('Інформація за хештегом:\n{}' if language == 'ukrainian' else 'Information about the hashtag:\n{}').format(hashtag.name) + '\n' + link
         except:
            print('Виникла помилка парсингу')
   except:
      return '😢 Сформуйте хештег іншим чином' if language == 'ukrainian' else '😢 Form a hashtag differently'

      

   