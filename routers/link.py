from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy.orm import Session

from database import config
from schemas.link import LinkInput, LinkOutput
from controllers import link

get_db = config.get_db

router = APIRouter()


@router.get('/{short}', response_model=LinkOutput, status_code=status.HTTP_200_OK)
async def get_link(short: str, db: Session = Depends(get_db)) -> LinkOutput:
    db_link = link.get(db, short)

    if db_link:
        return db_link
    
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Link Not Found!"
    )


@router.post('/', response_model=LinkOutput, status_code=status.HTTP_201_CREATED)
async def create_link(request: LinkInput, db: Session = Depends(get_db)) -> LinkOutput:
    db_link = link.create(db, request)

    if db_link:
        return db_link
    
    raise HTTPException(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        detail="Database Error!"
    )


@router.put('/{short}', response_model=LinkOutput, status_code=status.HTTP_201_CREATED)
async def update_link(short: str, request: LinkInput, db: Session = Depends(get_db)) -> LinkOutput:
    db_link = link.update(db, request, short)

    if db_link:
        return db_link
    
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Link Not Found!"
    )


@router.delete('/{short}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_link(short: str, db: Session = Depends(get_db)) -> None:
    db_link = link.delete(db, short)

    if db_link:
        return None
    
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Link Not Found!"
    )
