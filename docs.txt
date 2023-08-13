'''
apps parts:

    models.py !
    repository.py | managers.py | # запросы !
    services.py !
    schemas.py !(fastapi)
    routes.py !
    enums.py
    exception.py
    jobs.py


# FLSAK
apps: [posts, users, chats]


    models
        posts_models.py
        users_models.py
        chats_models.py
    repository
        posts_repository.py
        posts_tags_repository.py
        posts_comments_repository.py
        users_repository.py
        chats_repository.py
    services
        users_services.py
        chats_services.py
    schemas
        posts_schemas.py
        users_schemas.py
        chats_schemas.py
    routes
        posts_routes.py
        users_routes.py
        chats_routes.py
    enums
        chats_enums.py
    exception
        users_exception.py
        chats_exception.py
    jobs
        posts_jobs.py



# DJANGO

    posts
        comments
        posts
        likes
        tags
    users
    chats

    posts

        comments
            models.py !
            repository.py | managers.py | # запросы !
            services.py !
            schemas.py !(fastapi)
            routes.py !
            enums.py
            exception.py
            jobs.py
        posts
            models.py !
            repository.py | managers.py | # запросы !
            services.py !
            schemas.py !(fastapi)
            routes.py !
            enums.py
            exception.py
            jobs.py
        tags
            models.py !
            repository.py | managers.py | # запросы !
            services.py !
            schemas.py !(fastapi)
            routes.py !
            enums.py
            exception.py
            jobs.py


        models.py !
        repository
            comments.py
            post.py
            tags.py

        services
            comments.py
            post.py
            tags.py

        schemas.py
            comments.py
            post.py
            tags.py

        routes.py !
        enum s.py
        exception.py
        jobs.py
    users
        models.py !
        repository.py | managers.py | # запросы !
        services.py !
        schemas.py !(fastapi)
        routes.py !
        enums.py
        exception.py
        jobs.py
    chats
        models.py !
        repository.py | managers.py | # запросы !
        services.py !
        schemas.py !(fastapi)
        routes.py !
        enums.py
        exception.py
        jobs.py


/registration
server  <- {login: mike, pass: 1234}   front
server  pass_hash = hash(pass=1234, KEY)  -> "sdfsagasawbhr7hwvsdvsaft23fwge"
server  save_to_db(user, pass_hash) -> {id : 1}

        users
        id   |   name    |  password
         1   |   "mike"  |  "sdfsagasawbhr7hwvsdvsaft23fwge"

server  auth_key = gen_auth_key() -> "vu8sdhgwafbwaudgewhgnsdgsNFwERFNDSGEWFBYWSR3yufcaBOScaso"

        save_session(auth_key)

        session
        user_id id   |   auth_key                                                  | expire_time  | ...
            1        |   "2vu8sgwafbwaudgewhgsdfsgsscfsdfsdffdsdfWSR3yufcaBOScaso" | 12.11.2023   | android
            1        |   "3u8sdhgwafbwaasdsdgbsdgsdvsdvscDSGEWFBYWSR3yufcaBOScaso" | 12.11.2023   | ...

server -> {auth_key: auth_key, id: 1} front

front storage  = [auth_key,]


/post/1
server  <- Request(header {auth: auth_key})  front
server  middleware:  user = get_user_by_auth_key(auth) -> User
        >>> users_id = 'select user_id from session where auth_key = {auth} and expire_time > now()'
        >>> user = 'select * from user where id = {users_id}'
server  url < Request + user
...
...


/login
server  <- {login: mike, pass: 1234}   front
server
server  get_user_by_name("mike") -> Use | 404 | 401
server  pass_hash = hash(pass=1234, KEY)  -> "sdfsagasawbhr7hwvsdvsaft23fwge"
server  user.password == pass_hash >> OK | 401



JWT >>>

env KEY="vdsabhigsahnpgbadsbvbnadsvlnsadvnisdvnsdvnsdvljsdvujwSEFBJSDVBJLSDCBHLsadCLBHISDABLHSDCBL"

/registration
server  <- {login: mike, pass: 1234}   front
server   save_user_to_db()
         hash_pass()
         ...
server  save_to_db(user, pass_hash) -> {id : 1}

        users
        id   |   name    |  password
         1   |   "mike"  |  "sdfsagasawbhr7hwvsdvsaft23fwge"


server   auth_token = jwt.encode(data={id: 1, username: mike, expire_time: 10.11.23}, key=KEY) -> 'asfsfsdf.shupefwndvasgnasv.noasvdnlsdv'
server -> {auth_key: auth_token, id: 1} front
front storage = [auth_key,]

/post/1
server  <- Request(header {auth: auth_key})  front
server   jwt.decode(auth_key, key=KEY) -> {id: 1, username: mike, expire: 10.11.23}
            if expire < now(): rise 401
server   jwt.decode(wrong_auth_key, key=KEY ) -> JWTEncodeError


HTTPOnly Cookie
>>> Reponse(hettp_only_cookei={'auth': auth_key})


refresh_toke
>>> Reponse(hettp_only_cookei={'auth': auth_key, refresh_toke: gen_hash()})
server   jwt.decode(auth_key, key=KEY) -> {id: 1, username: mike, expire: 10.11.23}
            if expire < now():
                refresh_toke.decode() -> JWTEncodeError
`
>>> Reponse(hettp_only_cookei={'auth': new_auth_key, new_fefresh_toke: gen_hash()}








'''
