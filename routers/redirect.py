from fastapi import APIRouter, status, Depends, HTTPException
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session

from database import config
from controllers import link

get_db = config.get_db

router = APIRouter()


@router.get('/{short}', status_code=status.HTTP_301_MOVED_PERMANENTLY)
async def redirect(short: str, db: Session = Depends(get_db)) -> RedirectResponse:
    db_link = link.get(db, short)

    if db_link:
        return RedirectResponse(
            db_link.address,
            status_code=status.HTTP_301_MOVED_PERMANENTLY
        )

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Link Not Found!"
    )
