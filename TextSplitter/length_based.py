from langchain.text_splitter import CharacterTextSplitter
from dotenv import load_dotenv
from langchain_community.document_loaders import PyMuPDFLoader

load_dotenv()

loader=PyMuPDFLoader('TextSplitter\AgenticAI-v2.0.pdf')

docs=loader.load()

# text = """"
# LunarTree Software Development Intern Frontend Assignment TASK 
# For  this  task  we  require  you  to  create  a  simple  todo  list  app  using  Next.js  and 
# TailwindCSS.  The  goal  of  this  assignment  is  to  assess  your  foundational  knowledge 
# and  practical  skills.  The  todo  list  app  needs  to  be  a  fully  functional,  Kanban-style 
# application. 
# Your application should be single-page with the following core features: 
# 1.  
# Three  Status  Columns:  The  application  UI  must  clearly  display  three  distinct 
# columns for tasks based on their status - Pending, In Progress and Done. 
# 2.  Add  New  Todo:  A  clear  input  field  and  a  button  to  allow  users  to  add  new 
# tasks.  Newly  added  tasks  should  default  to  the  "Pending"  status.  Tasks  must 
# have a unique identifier. 
# 3.  Task  Management:  Each  task  card  should  display  the  task's  title  and 
# description.  Users  must  be  able  to  change  the  status  of  a  task  from  one 
# column  to  another  (e.g.,  from  "Pending"  to  "In  Progress",  or  "In  Progress"  to 
# "Done").  The  UI  should  reflect  these  changes  instantly.  Users  should  be  able  to 
# delete tasks. 
# 4.  Local  State  Persistence:  Implement  a  mechanism  to  store  the  Todo  list  data 
# locally  in  the  browser  (e.g.,  using  localStorage)  so  that  tasks  persist  even  after 
# the browser tab is closed and reopened. 
# 5.  Deployment:  The  application  should  be  deployed  on  your  choice  of  provider 
# (Cloudflare/Vercel/Heroku etc) and a working link shared with us. 
# (OPTIONAL  BONUS  FEATURES)  Consider  implementing  the  following  features  to 
# significantly improve the application's usability and efficiency: 
# 1.  
# Keyboard  navigation  and  shortcuts:  Allow  users  to  move  items  between 
# states and create/delete them efficiently using only their keyboard. 
# 2.  Drag-and-drop  functionality:  Enable  intuitive  movement  of  items  between 
# different states via drag and drop. 
# 3.  UI:  A clean, beautiful, and highly refined user interface. 
# NOTES 
# 1.  
# Please  don’t  use  AI  to  generate  code  (only  for  this  assignment,  if  selected  you 
# get to use the best that’s out there) 
# 2.  Create a public repository on github and do  atomic commits 
# """
splitter = CharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=0,
    separator=''
)

result = splitter.split_documents(docs)

print(result[0].page_content)
print(result[0].metadata)
