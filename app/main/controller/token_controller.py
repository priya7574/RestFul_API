from flask_restplus import Resource
from ..util.dto import TokenDto
from ..helper.token_helper import token_required
from ..service.token_service import create_token
api = TokenDto.api


@api.route('/')
class GenerateToken(Resource):
    # @api.expect(parser)
    @api.response(201, 'Successfully create token')
    @api.doc('create a access token')
    def get(self):
        """create access token """
        return create_token()
