#   c o d i n g = u t f 8 
 i m p o r t   s u b l i m e ,   s u b l i m e _ p l u g i n 
 
 c l a s s   E n c o d i n g P l u g i n ( s u b l i m e _ p l u g i n . E v e n t L i s t e n e r ) : 
         d e f   _ _ i n i t _ _ ( s e l f ) : 
                 r e t u r n 
         d e f   o n _ l o a d ( s e l f ,   v i e w ) : 
                 v i e w . s e t _ s t a t u s ( ' S h o w E n c o d i n g P l u g i n S t a t u s ' ,   v i e w . e n c o d i n g ( )   i f   v i e w . e n c o d i n g ( )   ! =   u ' U n d e f i n e d '   e l s e   s u b l i m e . l o a d _ s e t t i n g s ( ' P r e f e r e n c e s . s u b l i m e - s e t t i n g s ' ) . g e t ( ' d e f a u l t _ e n c o d i n g ' ,   ' U n k n o w n   E n c o d i n g ' ) ) 