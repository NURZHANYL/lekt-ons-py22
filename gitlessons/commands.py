# 1.GIT- распределение системы контроля версий
# 2.
# 3.
# 4.Репозиторий - хранилище ваших файлов который вы отслеживаете при помощи гита, и их изменение
# 5.
# 6.Команды Git
# 7.
# 8. 1.git init - она создает новый гит репозиторий локально на вашем пк, создаст она в той директории где вы запускаете эту команду (запускается только один раз)
#  9. 
# 10.2. Git add - когда мы создаем изменяем файлы то при помощи этой команды мы загружаем все измещения в промежуточные место хранение 
# 12.git add <file name>
# 13.git add . - все в текущей директорий 
# 14.
# 15. 3. git commit - как только мы достигаем до определенного момента в разработке, то мы тогда сохраняем и комментируем все наши изменения в репозиторий. 
# (Фиксация изменение в репо)
# 16. 
# 17. 
# 18. git commit -m '< >

# 4. git remote add - eto komanda dlya togo. chtoby svyazat vash lokalnyi repozitoriy s udalennym repozitoriem (epo v githube) < nazvanie podklyucheniya>  <ssylka na repozitoriy>



# git remote add origin <url>

# 5. git push - после коммита изменений при помощи этой команды мы отправляем наши изменения в файлах на удаленный репозиторий.

# git push < origin > >nazvanie vetki>

# git push origin main 

____________________________
1. git init 
2. git branch -M main (pereimenovyvaem glavnyuyu vetku s master na main)
3. git add . 
4. git commit -m 'comment' (vse dobavleno v lokal repo)
5. git remote add origin <url>
6. git push origin main 
/////////////////////

git add . 
git commit -m 'comment'
git push origin main 
