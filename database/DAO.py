from database.DB_connect import DBConnect
from model.album import Album


class DAO:
    def __init__(self):
        pass

    @staticmethod
    def getAlbum(durata):
        cnx=DBConnect.get_connection()
        cursor=cnx.cursor(dictionary=True)

        query="""select a.*,sum(t.Milliseconds)/60000 as durata
                from itunes.album a ,itunes.track t 
                where a.AlbumId =t.AlbumId 
                group by a.AlbumId ,a.Title ,a.ArtistId 
                having durata > %s"""
        cursor.execute(query,(durata,))

        risultato=[]
        for a in cursor:
            risultato.append(Album(**a))

        cursor.close()
        cnx.close()
        return risultato

    @staticmethod
    def getArchi(durata):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=False)

        query = """select distinctrow t1.AlbumId a1, t2.AlbumId a2
                    from (
                    select distinctrow  a.AlbumId ,pt.PlaylistId 
                    from itunes.track t  ,itunes.playlisttrack pt,
                    (select a.*
                    from itunes.album a ,itunes.track t 
                    where a.AlbumId =t.AlbumId 
                    group by a.AlbumId ,a.Title ,a.ArtistId 
                    having sum(t.Milliseconds)/60000 > %s) a
                    where a.AlbumId =t.AlbumId 
                    and pt.TrackId =t.TrackId ) t1,
                    (select distinctrow  a.AlbumId ,pt.PlaylistId 
                    from itunes.track t  ,itunes.playlisttrack pt,
                    (select a.*
                    from itunes.album a ,itunes.track t 
                    where a.AlbumId =t.AlbumId 
                    group by a.AlbumId ,a.Title ,a.ArtistId 
                    having sum(t.Milliseconds)/60000 > %s) a
                    where a.AlbumId =t.AlbumId 
                    and pt.TrackId =t.TrackId) t2
                    where t1.PlaylistId=t2.PlaylistId
                    and t1.AlbumId<t2.AlbumId
                    """
        cursor.execute(query, (durata,durata,))

        risultato = []
        for a in cursor:
            risultato.append(a)

        cursor.close()
        cnx.close()
        return risultato
