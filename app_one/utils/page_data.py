from django.utils.safestring import mark_safe
from app_one import models
from copy import deepcopy
from urllib.parse import urlencode


class PageData:
    """get data object"""
    def __init__(self, request, queryset, page_size=10, edge=2, _page_param="page"):
        self.request = deepcopy(request.GET)
        self.queryset = queryset
        self.page_size = page_size
        self.edge = edge
        self.page_param = _page_param

        # in case invalid page param
        page = str(request.GET.get(self.page_param, 1))
        if page.isdecimal():
            page = int(page)
        else:
            page = 1
        self.page = page
        
        # confirm start page and end page
        self.start_page = (page - 1) * page_size
        self.end_page = page * page_size
        self.data_list = queryset[self.start_page: self.end_page]
        self.data_asset_count = queryset.count()

        # calculate page amount
        fullpage_count = self.data_asset_count // page_size
        page_count = fullpage_count if self.data_asset_count % page_size==0 else fullpage_count + 1
        self.page_count = page_count

        self.page_htmlgen()
    

    def page_htmlgen(self):
        # generate page html
        if self.page_count < 2*self.edge + 1:
            # only few pages
            start_page = 1
            end_page = self.page_count
        elif self.page <= self.edge:
            # first few pages
            start_page = 1
            end_page = 2*self.edge + 1
        elif self.page > self.page_count - self.edge:
            # last few pages
            start_page = self.page_count - self.edge * 2
            end_page = self.page_count
        else:
            start_page = self.page - self.edge
            end_page = self.page + self.edge
        
        page_str_list = []
    
        """ 
        main page list bar
        template: 
        new_html()
        href_section = self.request.setlist(self.page_param, [new_element])
        <li class="[li_class=page-link]">
            <a class="page-link" href="?{herf_section}">
                [text]
            </a>
        </li>                  
        """
        # start page
        page_str_list.append(self.new_html(1,"First page"))
        
        # previous page
        previous_page = self.page
        if self.page >= 2:
            previous_page -= 1
        page_str_list.append(self.new_html(previous_page,"previous"))
        
        # around current page
        for page_num in range(start_page, end_page+1):
            page_class = "page-item"
            if page_num == self.page:
                page_class += " active"
            page_str_list.append(self.new_html(page_num,page_num,li_class=page_class))
        
        # next page
        next_page = self.page
        if self.page + 1 <= self.page_count:
            next_page += 1
        page_str_list.append(self.new_html(next_page,"next"))

        # end page
        page_str_list.append(self.new_html(self.page_count,"Lastpage"))

        # search field
        search_field = '''
                        <li class="page-item">
                            <form id="searchForm" method="get" role="search" class="d-flex align-items-center">
                                <input class="page-link" type="number" name="page" placeholder="#"
                                aria-label="Search" style="width: 100px;" id="skipToInput" min="1">
                                <button class="btn btn-success ms-2" type="submit">
                                    Jump
                                </button>
                            </form>
                        </li> 
                        '''
        page_str_list.append(search_field)

        self.page_html = mark_safe("".join(page_str_list))
    

    def new_html(self, 
                 new_element,
                 text,
                 li_class="page-item",
                 ):
        self.request.setlist(self.page_param, [new_element])
        num_bar_template = f'''
                    <li class="{li_class}">
                        <a class="page-link" href="?{ self.request.urlencode() }">
                            {text}
                        </a>
                    </li>
                    '''
        return num_bar_template
    

    def get_pagehtml(self):
        # print(self.page_html, "对象内获取html字符串完成")
        return self.page_html
    

    def get_queryset(self):
        return self.data_list
        

